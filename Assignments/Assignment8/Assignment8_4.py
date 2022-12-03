def Add(No):
    Sum = 0
    for i in str(No) :
        Sum += int(i)
    return Sum


def main():
    A = int(input("Enter Number : "))
    Ans = Add(A)
    print("Addition is : ",Ans)



if __name__ == "__main__":
    main()