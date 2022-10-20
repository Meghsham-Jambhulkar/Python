#Write a program which contains one lambda function 
#which accepts one parameter and return power of two


def main():
    print("Enter a number :")
    No = int(input())

    Square = lambda A : A**2 

    Ans = Square(No)

    print("Square of given number is : ",Ans)







if __name__ =="__main__":
    main()