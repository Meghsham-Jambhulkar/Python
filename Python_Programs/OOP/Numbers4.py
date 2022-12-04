#Write a Program aceept n numbers from user 
#And Return Minimum of that N numbers 

class Numbers:

    def __init__(self):
        self.iSize = 0
        self.Arr= list()

    def Accept(self):
        print("Enter a number to set Limit : ")
        self.iSize = int(input())
        print("Enter Data")
        for i in range (0, self.iSize):
                No = int(input())
                self.Arr.append(No)
    def Display(self):
        print("Inserted Data is : ")
        for i in range(0,self.iSize):
            print(self.Arr[i])

        #print(self.Arr)

    def Summation(self):
        Sum = 0
        for i in range(0,self.iSize):
            Sum += self.Arr[i]
        return Sum

    def Average(self):
        Avg = 0
        Sum = 0
        for i in range(0,self.iSize):
            Sum += self.Arr[i]
        Avg = Sum/self.iSize
        return Avg

    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0 , self.iSize):
            if (self.Arr[i]>Max):
                Max = self.Arr[i]

        return Max

    def Minimum(self):
        Min = self.Arr[0]
        for i in range(0 , self.iSize):
            if (self.Arr[i]<Min):
                Min = self.Arr[i]

        return Min

            
        
        
def main():
    obj = Numbers()

    obj.Accept()
    obj.Display()

    Output = obj.Summation()
    print("Summation of all Elements is :",Output)

    Output = obj.Average()
    print("Average of all Elements is :",Output)

    Output = obj.Maximum()
    print("Maximum of all Elements is :",Output)

    Output = obj.Minimum()
    print("Minimum of all Elements is :",Output)

    Obj1 = Numbers()

    Obj1.Accept()
    Obj1.Display()

    
    Output = Obj1.Summation()
    print("Summation of all Elements is :",Output)

    Output = Obj1.Average()
    print("Average of all Elements is :",Output)

    Output = Obj1.Maximum()
    print("Maximum of all Elements is :",Output)

    Output = Obj1.Minimum()
    print("Minimum of all Elements is :",Output)



if __name__ == "__main__":
    main()