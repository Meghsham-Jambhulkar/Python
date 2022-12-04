def Display(No):

    if (No > 0):
        No -= 1
        Display(No) #Head Recursion when it not at end
        print(No)

Display(4)