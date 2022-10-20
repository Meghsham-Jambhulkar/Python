#Write a program which input from user and create a list 
#filter list of numbers greater than or equal to 70 and less than or equal to 90 
#add 10 in those list items and return product of those list elements


from functools import reduce

ChkData = lambda No : No >= 70 and No <=90

# def FilterX(Data):
#     Data_Filter = []
#     for i in Data:
#         if (i >= 70 and i <=90):
#             Data_Filter.append(i)

#     return Data_Filter

Add = lambda A : A + 10

# def MapX(Data_Filter):
#     Data_Map = []
#     for i in Data_Filter:
#         i += 10
#         Data_Map.append(i)
#     return Data_Map

prod = lambda A , B: A*B


# def ReduceX(Data_Map):
#     prod = 1
#     for i in Data_Map:
#         prod = prod * i
#     return prod
            


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

    Data_Map = list(map(Add ,Data_Filter))

    print("Mapped List :",Data_Map)

    print("_____________________________________________________")

    Data_Reduce = reduce(prod,Data_Map)

    print("Reduced List :",Data_Reduce)

if __name__ == "__main__":
    main()