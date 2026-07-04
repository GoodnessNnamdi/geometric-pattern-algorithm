for i in range(5, 0, -1):
    left_side = "  " * (5 - i) + " ".join("*" * (2 * i - 1))
    right_side = "    " * (5 - i) + " ".join("*" * (2 * i - 1))
    print(left_side + " " + right_side)