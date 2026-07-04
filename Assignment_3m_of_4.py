for i in range(1, 5 + 1):
        left_side = "  " * (5 - i) + " *" * (2 * i - 1)
        right_side = "    " * (5 - i) + " *" * (2 * i - 1)
        print(left_side + "" + right_side)
