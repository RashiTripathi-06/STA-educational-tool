#Multi-path STA using a simple engine

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sta_engine import compute_Tcomb, check_setup, check_hold, build_graph
from circuit_models import example_multi_path_circuit
from graph_utils import find_all_paths



# Main STA Flow
if __name__ == "__main__": 

    # Load circuit
    edges, launch_ff, capture_ff = example_multi_path_circuit() 
    graph, delays = build_graph(edges)

    # Timing parameters
    Tclk = 10.0
    Tcq = 1.0
    Tsetup = 2.5
    Tcq_min = 0.5
    Thold = 1.0

    paths = find_all_paths(graph, launch_ff, capture_ff) 

    print("\n=== Running Multi-Path STA ===\n")

    worst_setup_slack = float("inf")
    critical_path = None

    for path in paths:
        print("Path:", " -> ".join(path)) #.join is used to convert list to string with separator " -> "

        Tcomb = compute_Tcomb(path, delays)

        setup_slack = check_setup(Tclk, Tcq, Tcomb, Tsetup) 
        hold_slack = check_hold(Tcq_min, Tcomb, Thold)

        print(f"  Tcomb       = {Tcomb:.2f} ns")
        print(f"  Setup slack = {setup_slack:.2f} ns")
        print(f"  Hold slack  = {hold_slack:.2f} ns")

        if setup_slack < worst_setup_slack:
            worst_setup_slack = setup_slack
            critical_path = path

        if setup_slack < 0:
            print("Setup violation")

        if hold_slack < 0:
            print("Hold violation")

        print()

    print("STA SUMMARY")
    print("Critical Path:")
    print(" -> ".join(critical_path))
    print(f"Worst Setup Slack = {worst_setup_slack:.2f} ns")


# ===================== STA CALCULATION (THIS CIRCUIT) =====================

# Paths found:
# 1) FF1 → G1 → G2 → FF2
# 2) FF1 → G1 → FF3 → G2 → FF2

# --------------------- Tcomb ---------------------
# Path 1:
#   = 1.5 + 2.0 + 3.0 = 6.5 ns
#
# Path 2:
#   = 1.5 + 1.0 + 0.8 + 3.0 = 6.3 ns

# --------------------- SETUP SLACK ---------------------
# Formula:
#   Setup Slack = Tclk - (Tcq + Tcomb + Tsetup)

# Path 1:
#   = 10 - (1 + 6.5 + 2.5)
#   = 10 - 10
#   = 0 ns  → borderline PASS

# Path 2:
#   = 10 - (1 + 6.3 + 2.5)
#   = 10 - 9.8
#   = 0.2 ns  → PASS

# --------------------- HOLD SLACK ----------------------
# Formula:
#   Hold Slack = (Tcq_min + Tcomb) - Thold

# Path 1:
#   = (0.5 + 6.5) - 1
#   = 7.0 - 1
#   = 6.0 ns  → PASS

# Path 2:
#   = (0.5 + 6.3) - 1
#   = 6.8 - 1
#   = 5.8 ns  → PASS

# --------------------- CRITICAL PATH ---------------------
# Path with minimum setup slack:
#   FF1 → G1 → G2 → FF2 (Setup Slack = 0 ns)

# ========================================================================