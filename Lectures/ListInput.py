def main():

    Arr =  list()

    print("Enter How many elements you want to store : ")
    size = int(input())
    print("Enter element to enter in list :")
    for i in range(0,size):

        Arr.append(int(input()))

    print(Arr)

    print(" Insert Element at specific index")
    print("Enter Index :")
    id = int(input())
    print("Enter Value :")
    val= int(input())
    if id < len(Arr):
        Arr.insert(id,val)
        print(Arr)
    else :
        print("Out of index will insert at last ")
        Arr.insert(id,val)
        print(Arr)
if __name__ == "__main__":
    main()