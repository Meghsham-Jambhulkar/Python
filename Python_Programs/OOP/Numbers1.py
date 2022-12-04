#Write a Program aceept n numbers from user 
#And Return Addition of that N numbers 

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
            
        
        
def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()
    Output = obj.Summation()
    print("Summation of all Elemens is :",Output)

    Output = obj.Average()
    print("Average of all Elemens is :",Output)
if __name__ == "__main__":
    main()