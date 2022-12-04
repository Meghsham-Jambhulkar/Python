#Take List filter even numbers add two in each element
#and add of them after it

def CheckEven(No):
    return (No % 2 == 0)

def Increament(No):
    return No+2

def FilterX(arr,Function_Name):
    result = []
    for no in arr:
        if (Function_Name(no)):
            result.append(no)
    return result

def mapX(arr,Function_Name):
    Result = []
    for no in arr:
        value = Function_Name(no)
        Result.append(value)
    return Result
    
def reduceX(arr):
    sum = 0
    for no in arr :
        sum = sum + no
    return sum



def main():
    Data = [2,3,1,6,4,5,11,16,20]
    print("Original Data : ",Data)

    Data_Filter = list(FilterX(Data,CheckEven))

    print("Data After Filter : ",Data_Filter)
    
    Data_Map = list(mapX(Data_Filter,Increament))
    print("After Map : ",Data_Map)

    ret = reduceX(Data_Map)
    print("Data after Reduce :",ret)
if __name__ == "__main__":
    main()