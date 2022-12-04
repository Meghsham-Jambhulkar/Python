def main():
    print("Enter number ")
    no = int(input())
    print("Factors are : ")
    for i in range (1,int(no/2)+1):
        if no % i == 0:
            print(i,end=" ")





if __name__ == "__main__":
    main()