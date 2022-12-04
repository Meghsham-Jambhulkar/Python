from cgi import print_arguments


def main():
    
    # Data : Heterogeneous
    # Ordered : Yes
    # Indexed : Yes
    # Mutable : No
    # Duplicates : Yes

    Data = (11,21,51,101)
    print("_________________")

    print("output Using For :")
    for no in Data :
        print(no, end =" ")
    print("\n_______________________")


    print("output Using For with index  :")
    for i  in range (0,len(Data)) :
        print(Data[i] , end =" ")
    print("\n_______________________")

    print("output Using While with index  :")
    i = 0
    while (i < len(Data)):
        print(Data[i] , end =" ")
        i += 1
    print("\n_______________________")

if __name__ == "__main__":
    main()