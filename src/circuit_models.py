# Circuit descriptions(user-defined)

def example_multi_path_circuit():
    """
    Returns:
    edges       : (src, dst, delay)
    launch_ff   : launch flip-flop
    capture_ff  : capture flip-flop
    """

    edges = [
        ("FF1", "G1", 1.5),
        ("G1", "G2", 2.0),
        ("G2", "FF2", 3.0),

        # parallel path
        ("G1", "FF3", 1.0),
        ("FF3", "G2", 0.8)
    ]

    launch_ff = "FF1"
    capture_ff = "FF2"

    return edges, launch_ff, capture_ff
