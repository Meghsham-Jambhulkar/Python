#Write a program which accept N number from user
#and Stores it into List . Return Addition of all prime numbers from that list 

def ChkPrime(Data):
    Sum = 0 
    prime = []
    for i in Data:
        r =  0 
        for j in range (1,i):
            if i%j == 0:
                r+= 1
        if r == 1:
            prime.append(i)

    print("Prime numbers from lists are : ",prime)
    ans = sum(prime)
    return ans
       
def main():
    print("Enter a Number to set limit to Input : ")
    iSize = int(input())
    print("Enter Data : ")
    Data = []
    for i in range (0 , iSize):
        Value = int(input())
        Data.append(Value)
    print("List after Insertion of Data : ",Data)
     
    Ans = ChkPrime(Data)
    print("The Addition of all prime elements in List is : ",Ans)



if __name__ == "__main__":
    main()