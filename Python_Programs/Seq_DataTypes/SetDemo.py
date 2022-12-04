def main():
    print("Demonstration of Set")

    # Data : Heterogeneous
    # Ordered : No
    # Indexed : No
    # Mutable : Yes
    # Duplicates : No
    #kenth thompson
    #linus stonewalon

    data={11,21,51,101}
    data1 = {11,90.80,True,"Hello"} #Heterogeneous

    print("Data is Heterogeneous : ",data1)

    print("List is mutable")
    data.add(201)
    print("List after append : ",data)
    data.pop()
    print("Data after pop : ",data)
if __name__ == "__main__":
    main()