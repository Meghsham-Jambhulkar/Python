def main():
    print("Demonstration of list")

    # Data : Heterogeneous
    # Ordered : Yes
    # Indexed : Yes
    # Mutable : Yes
    # Duplicates : Yes
    #kenth thompson
    #linus stonewalon

    data=[11,21,51,101,51,21,11]
    data1 = [11,90.80,True,"Hello"] #Heterogeneous

    print("Data is Heterogeneous : ",data1)
    print("Data is Ordered : ",data)
    print("Data at index 2 :",data1[2])
    print("Data with duplicate elements : ",data)

    print("List is mutable")
    data.append(201)
    print("List after append : ",data)
    data.pop()
    print("Data after pop : ",data)
if __name__ == "__main__":
    main()