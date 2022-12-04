def main():

    try:
        print("Enter first number :")
        No1 = int(input())

        print("Enter second number :")
        No2 = int(input())

    
        Ans = No1 / No2
        print("Division is : ",Ans)

    except ZeroDivisionError :
        print("Inside zero division error")

    except ValueError :
        print("Inside Value error ")

    except Exception:
        print("Inside Last Exception block")

    finally:
        print("Inside Finally Block")
        




if __name__ =="__main__":
    main()