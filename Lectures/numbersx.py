def DisplayFactors(no):
    i = 1
    while (i <= int(no/2)):
        if (no % i == 0): 
            print(i)
        i += 1 
