def Add(*Values ): 
    sum = 0
    for i in Values:
        sum = sum + i 
    return sum

def AddX(*Values ): 
    sum = 0
    for i in range(0,len(Values)):
        sum = sum + Values[i] 
    return sum

def main():
    ans = AddX(1,7,9,4,6,5)
    print("Addition is : ",ans)



if __name__ =="__main__":
    main()