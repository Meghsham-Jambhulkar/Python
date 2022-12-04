#Normal / Named Function
def Add(No1, No2):
    return No1+No2

#Lambda Function / Unnamed Fuction
#Syntax : lambda parameter : body

AddFunction = lambda A,B : A+B

def main():
    Ans1 = Add(10,11)
    Ans2 = AddFunction(10,11)

    print("Addition using normal Function : ",Ans1)
    print("Addition using Lambda Function : ",Ans2)
    print("Type of Lambda Function : ",type(AddFunction))

if __name__ == "__main__":
    main()