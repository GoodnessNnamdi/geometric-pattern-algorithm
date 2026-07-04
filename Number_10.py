for r in range(5):
    for c in range(4 - r):
        print (" ", end = " ")
    for c in range(r + 1):
         print("*", end = " ")
         
    print()