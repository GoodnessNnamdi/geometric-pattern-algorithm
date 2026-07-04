# First, build your original hourglass into a list of strings
hourglass = []
for i in range(7, 0, -1):
    spaces = "  " * (7 - i)
    stars = "  ".join("*" * i)
    hourglass.append(spaces + stars)

for i in range(2, 7 + 1):
    spaces = "  " * (7 - i)
    stars = "  ".join("*" * i)
    hourglass.append(spaces + stars)

# Pad all rows to the same width
max_width = max(len(row) for row in hourglass)
padded = [row.ljust(max_width) for row in hourglass]

# Rotate 90° clockwise: print column by column
for col in range(max_width):
    new_row = "".join(padded[row][col] for row in range(len(padded)))
    print(new_row)
