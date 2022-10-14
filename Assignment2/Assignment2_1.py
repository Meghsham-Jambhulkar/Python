#Write on python program which call all the functions from arithmetic module by accepting 
#the parameters from user

import Arithmetic

def main():
    print("Enter First Number :")
    no1 = int(input())
    print("Enter Second Number : ")
    no2 = int(input())
    
    add = Arithmetic.Addition(no1,no2)
    sub = Arithmetic.Substraction(no1,no2)
    mult = Arithmetic.Multiply(no1,no2)
    div = Arithmetic.Division(no1,no2)

    print("Addition of two numbers is :",add)
    print(" ")
    print("Substraction of two numbers is :",sub)
    print(" ")
    print("Multiplication of two numbers is :",mult)
    print(" ")
    print("Division of two numbers is :",int(div))

if __name__ == "__main__":
    main()