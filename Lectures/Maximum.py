#Application to Findout Maximum Number 
def Maximum(Value1 , Value2):
    if(Value1 > Value2):
        return Value1
    else:
        print("Both Are Equal ")
        return Value1

def main():

    print("Enter First Number : ")
    no1 = input()

    print("Enter Second Number : ")
    no2 = input()

    Ans = Maximum(int(no1),int(no2))

    print("Largest Number is :",Ans)
    

if __name__ == "__main__":
    main()