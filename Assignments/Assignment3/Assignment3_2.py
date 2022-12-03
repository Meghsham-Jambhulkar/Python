#Write a program which accept N number from user
#and Stores it into List . Return Maximum from of all Elements from that list 

def main():
    print("Enter a Number to set limit to Input : ")
    iSize = int(input())
    print("Enter Data : ")
    Data = []
    for i in range (0 , iSize):
        Value = int(input())
        Data.append(Value)
    print("List after Insertion of Data : ",Data)
     
    Ans = max(Data)
    print("The Maximum from all elements in List is : ",Ans)



if __name__ == "__main__":
    main()