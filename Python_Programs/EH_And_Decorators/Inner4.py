def Substraction(No1,No2):

    Ans = 0
    Ans = No1 - No2

    return Ans 


def Decorated_Function(Function_Name):
    def Inner(A,B):
        if ( A < B ):
            print("Before swap :",A,B)
            A, B = B , A
            print("After swap :",A,B)
        return Function_Name(A,B)

    return Inner


def main():
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))

    New_Function = Decorated_Function(Substraction)
    ret = New_Function(Value1,Value2)

    print("Substraction is " ,ret)

if __name__ == "__main__":
    main()