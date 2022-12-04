#Positional Arguments 
def Add1(No1,No2):
    print("Value of No1 : ",No1 )
    print("Value of No2 : ",No2)
    
    return No1 + No2 
#Keyword Arguments
def Sub1(No1,No2):
    print("Value of No1 : ",No1 )
    print("Value of No2 : ",No2)
    return No1 - No2 


def main():
    ans = Add1(10,11)
    print("Addition is : ", ans)
    print("_______________________")
    ans = Sub1(No1=10,No2=11)
    print("Substraction is : ", ans)
    print("_______________________")
    ans = Sub1(No2=10,No1=11)
    print("Substraction is : ", ans)
    print("_______________________")
if __name__ == "__main__":
    main()