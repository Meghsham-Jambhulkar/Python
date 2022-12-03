#Write a program which accept N number from user
#and Stores it into List . Return Frequency of number from all Elements of that list 

from queue import PriorityQueue


def Count(Data):
    print("Enter a Number to know the Count : ")
    value = int(input())
    itr = 0
    for i in Data :
        while( i == value):
            itr += 1
            i+= 1
    return itr
    
                



def main():
    print("Enter a Number to set limit to Input : ")
    iSize = int(input())
    print("Enter Data : ")
    Data = []
    for i in range (0 , iSize):
        Value = int(input())
        Data.append(Value)
    print("List after Insertion of Data : ",Data)
     
    Ans = Count(Data)
    print("The Count of element in List is : ",Ans)



if __name__ == "__main__":
    main()