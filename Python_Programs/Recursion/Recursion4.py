def Display(No):
    print(No)

    if (No > 0):
        No -= 1
        Display(No)     # Tail Recursion when it at end

Display(4)