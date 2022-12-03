#Write a program which contains one function named as Add() which accepts two numbers 
#from user and return addition of that two numbers
def Addition(value1 , value2):
    Ans = value1 + value2
    return Ans

def main():
    print("Enter First Number")
    no1 = int(input())
    print("Enter Second Number ")
    no2 = int(input())

    ans = Addition(no1,no2)

    print("Sum of two numbers is : ",ans)

if __name__ == "__main__":
    main()