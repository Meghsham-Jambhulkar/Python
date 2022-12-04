from cgi import print_arguments


def main():
    
    # Data : Heterogeneous
    # Ordered : No
    # Indexed : No
    # Mutable : Yes
    # Duplicates : No

    Data = {11,21,51,101}
    print("_________________________")

    print("Output Using For :")
    for no in Data :
        print(no, end =" ")
    print("\n_______________________")

if __name__ == "__main__":
    main()