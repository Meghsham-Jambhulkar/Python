print("Application to demonstrate Industrial Programming")

import MarvellousModule 

def main():  
    print("value of __name__ from main is :",__name__)      
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    Sum = MarvellousModule.Addition(no1,no2)    
    print("Addition is :",Sum)


if __name__ == "__main__":
    main()