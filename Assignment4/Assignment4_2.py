#Write a program which contains one lambda function 
#which accepts two parameters and return multiplication of both


def main():
    print("Enter first number :")
    No1 = int(input())

    print("Enter Second number :")
    No2 = int(input())

    Mult = lambda A , B: A*B

    Ans = Mult(No1,No2)

    print("Multiplication of given numbers is : ",Ans)







if __name__ =="__main__":
    main()