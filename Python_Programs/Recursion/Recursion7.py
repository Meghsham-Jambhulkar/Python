#Factorial 


def Fact(No):
    if(No <= 0 ):
        return 1
    else:
        return(No * Fact(No-1))

def main():
    A = int(input("Enter Number : "))
    Ans = Fact(A)
    print("Factorial is : ",Ans)



if __name__ == "__main__":
    main()