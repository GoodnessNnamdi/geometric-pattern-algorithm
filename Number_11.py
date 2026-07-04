# for i in range(1, 6 + 1):
#         print(" *" * i + "  " * (6 - i) + "* " * i)
# for i in range(6 - 1, 0, -1):
#         print(" *" * i + "  " * (6 - i) + "* " * i)

for i in range(1, 5 + 1):
        print(" *" * i)
for r in range(5):
    for c in range(4 - r):
        print (" ", end = " ")
    for c in range(r + 1):
         print("*", end = " ")
         
