#Write a program which input from user and create a list 
#filter list of numbers which are prime
#Multiply those elements by 2 and return maximum of those list elements

def FilterX(Data):
    Data_Filter = []
    flag = True
    for i in Data:
        if i == 2:
                Data_Filter.append(i)
        else :
            for j in range(2,i):
                if i%j == 0 :
                    flag = True
                    break
                else:
                    flag = False
                    break
            if flag == False: 
                Data_Filter.append(i)
    return Data_Filter

def MapX(Data_Filter):
    Data_Map = []
    for i in Data_Filter:
        i = i *2
        Data_Map.append(i)
    return Data_Map
    
def ReduceX(Data_Map):
    Maximum = max(Data_Map)
    return Maximum
            


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
    
    Data_Filter = list(FilterX(Data))

    print("Filtered List is :",Data_Filter)

    print("_____________________________________________________")

    Data_Map = list(MapX(Data_Filter))

    print("Mapped List :",Data_Map)

    print("_____________________________________________________")

    Data_Reduce = ReduceX(Data_Map)

    print("Reduced List :",Data_Reduce)

if __name__ == "__main__":
    main()