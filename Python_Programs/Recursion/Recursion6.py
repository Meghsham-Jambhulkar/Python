# 4
# 4 + 3+ 2 + 1 -> 10



def Add(No):
    if(No <= 0 ):
        return 0
    else:
        return(No + Add(No-1))

def main():
    A = int(input("Enter Number : "))
    Ans = Add(A)
    print("Summation is : ",Ans)



if __name__ == "__main__":
    main()