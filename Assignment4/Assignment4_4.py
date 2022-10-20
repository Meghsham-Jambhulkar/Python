#Write a program which input from user and create a list 
#filter list of numbers which are even
#find squares of those in those list items and return sum of those list elements


from functools import reduce

ChkData = lambda No : (No % 2 == 0)

sqr = lambda A : A**2

Sum = lambda A , B: A+B       


def main():
    print("Enter number to set limit of list : ")
    iSize = int(input())
    Data = []
    print("Enter Data : ")
    for i in range( 0 , iSize ) :
        val = int(input())
        Data.append(val)
    print("List After Entering Data : ",Data)
    print("_____________________________________________________")
    
    Data_Filter = list(filter (ChkData ,Data))

    print("Filtered List is :",Data_Filter)

    print("_____________________________________________________")

    Data_Map = list(map(sqr ,Data_Filter))

    print("Mapped List :",Data_Map)

    print("_____________________________________________________")

    Data_Reduce = reduce(Sum,Data_Map)

    print("Reduced List :",Data_Reduce)

if __name__ == "__main__":
    main()