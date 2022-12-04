from operator import truediv


def CheckEven(No):
    if (No%2 ==0):
        return True
    else:
        return False

def CheckEvenX(no):
    return (no % 2 == 0)

Even = lambda No : No%2 == 0

def main():
    ret = CheckEvenX(12)

    if (ret == True):
        print("Its Even")
    else:
        print("Its Odd")

    ans = Even(12) 
    if ans == True :
        print("It is Even")

    



if __name__ == "__main__":
    main()