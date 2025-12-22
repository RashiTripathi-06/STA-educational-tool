# Example usage (single-path STA)
# Run this file directly to see example STA calculations

from sta_engine import compute_Tcomb, check_setup, check_hold

if __name__ == "__main__":
#Run the code below only if this file is executed directly, NOT if it is imported by another file.”

    # timing path (order of data flow)
    path = ["FF1", "G1", "G2", "FF2"]  # Order matters in a timing path, so we use a LIST not dict
    print("Timing path:")
    for block in path:
        print(block)

    # delays between blocks (in ns)
    delays = {  # used a DICT to map (start_block, end_block) [tuple used] -> delay
        ("FF1", "G1"): 1.5,
        ("G1", "G2"): 2.0,
        ("G2", "FF2"): 3.0
    }

    Tcomb = compute_Tcomb(path, delays)
    print("Total combinational delay =", Tcomb, "ns")

    # Setup time parameters
    Tclk = 10.0    # clock period
    Tcq = 1.0      # clock-to-Q
    Tsetup = 2.5   # setup time

    setup_slack = check_setup(Tclk, Tcq, Tcomb, Tsetup)
    print("Setup slack =", setup_slack, "ns")

    if setup_slack >= 0:
        print("SETUP CHECK: PASS")
    else:
        print("SETUP CHECK: FAIL(Setup violation)")

    # Hold time parameters
    Tcq_min = 0.5   # minimum clock-to-Q delay
    Thold = 1.0     # hold time

    # For now, assume minimum combinational delay = Tcomb
    Tcomb_min = Tcomb

    hold_slack = check_hold(Tcq_min, Tcomb_min, Thold)
    print("Hold slack =", hold_slack, "ns")

    if hold_slack >= 0:
        print("HOLD CHECK: PASS")
    else:
        print("HOLD CHECK: FAIL(hold violation)")
