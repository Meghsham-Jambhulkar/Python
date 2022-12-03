#Write a program which accept N number from user
#and Stores it into List . Return Addition of all Elements from that list 

def Sum(Data):
    Sum = 0 
    for i in Data:
        Sum = Sum + i
    
    return Sum

def main():
    print("Enter a Number to set limit to Input : ")
    iSize = int(input())
    print("Enter Data : ")
    Data = []
    for i in range (0 , iSize):
        Value = int(input())
        Data.append(Value)
    print("List after Insertion of Data : ",Data)
     
    Ans = Sum(Data)
    print("The Addition of all elements in List is : ",Ans)



if __name__ == "__main__":
    main()