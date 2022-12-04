def main():
    print("Demonstration of Tuple")

    # Data : Heterogeneous
    # Ordered : Yes
    # Indexed : Yes
    # Mutable : No
    # Duplicates : Yes

    #kenth thompson
    #linus stonewalon

    data=(11,21,51,101,51,21,11)
    data1 = (11,90.80,True,"Hello")#Heterogeneous

    print("Data is Heterogeneous : ",data1)
    print("Data is Ordered : ",data)
    print("Data at index 2 :",data1[2])
    print("Data with duplicate elements : ",data)

if __name__ == "__main__":
    main()