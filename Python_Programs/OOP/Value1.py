#Write A Program to take number from user 
#And Determine It is Perfect or Not 

class Value:

    def __init__(self,Data):
        self.No = Data


    def SumFactors(self):
        Sum = 0

        for i in range (1 ,int(self.No/2)+1):
            if (self.No%i == 0):
                Sum += i

        return Sum


    def CheckPerfect(self):
        Ans = self.SumFactors()

        if (self.No == Ans):
            return True

        else:
            return False

            








def main():
    print("Please enter a Number")
    A = int(input())

    obj = Value(A)
    Sum = obj.SumFactors()
    print("Sum of Factors : ",Sum)

    ret = obj.CheckPerfect()
    if ret == True:
        print("{} is A  perfect Number ".format(A))
    else:
        print("{} is A Not perfect Number ".format(A))

    
    


if __name__ == "__main__":
    main()
    
    
