# EduSTA - Educational Static Timing Analysis Tool


# 1: Defining timing path (order of data flow)
path = ["FF1", "G1", "G2", "FF2"] #Order matters in a timing path, so we use a LIST not dict
print("Timing path:")
for block in path:
    print(block)

# 2: Define delays between blocks (in ns)
delays = { #used a DICT to map (start_block, end_block) [tuple used] -> delay
    ("FF1", "G1"): 1.5, 
    ("G1", "G2"): 2.0,
    ("G2", "FF2"): 3.0
}

#  Func to compute Tcomb
def compute_Tcomb(path, delays):
    Tcomb = 0
    for i in range(len(path) - 1): #len(path) = 4
        start = path[i]
        end = path[i + 1]
        Tcomb = Tcomb + delays[(start, end)]
    return Tcomb


Tcomb = compute_Tcomb(path, delays)
print("Total combinational delay =", Tcomb, "ns")


# 3: Setup time check
Tclk = 10.0   # clock period
Tcq = 1.0     # clock-to-Q (time taken by FF to change its output Q after the active clk edge arrives)
Tsetup = 2.5  # setup time


# func for setup check
def check_setup(Tclk, Tcq, Tcomb, Tsetup):
    setup_slack = Tclk - (Tcq + Tcomb + Tsetup)
    return setup_slack


setup_slack = check_setup(Tclk, Tcq, Tcomb, Tsetup)
print("Setup slack =", setup_slack, "ns")

if setup_slack >= 0:
    print("SETUP CHECK: PASS")
else:
    print("SETUP CHECK: FAIL(Setup violation)")


# Step 4: Hold time check
Tcq_min = 0.5     # minimum clock-to-Q delay in ns
Thold = 1.0       # hold time in ns

# For now, assume minimum combinational delay = Tcomb
Tcomb_min = Tcomb
# func for hold check
def check_hold(Tcq_min, Tcomb_min, Thold):
    hold_slack = (Tcq_min + Tcomb_min) - Thold
    return hold_slack


hold_slack = check_hold(Tcq_min, Tcomb_min, Thold)
print("Hold slack =", hold_slack, "ns")

if hold_slack >= 0:
    print("HOLD CHECK: PASS")
else:
    print("HOLD CHECK: FAIL(hold violation)")
