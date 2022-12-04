from cgi import print_arguments


def main():
    
    # Data : Heterogeneous
    # Ordered : Yes
    # Indexed : Yes
    # Mutable : Yes
    # Duplicates : Yes

    Data = [ 11,21,51,101]

    print("output Using For :")
    for no in Data :
        print(no, end =" ")
    print()


    print("output Using For with index  :")
    for i  in range (0,len(Data)) :
        print(Data[i] , end =" ")
    print()

    print("output Using While with index  :")
    i = 0
    while (i < len(Data)):
        print(Data[i] , end =" ")
        i += 1
    print()




    




if __name__ == "__main__":
    main()