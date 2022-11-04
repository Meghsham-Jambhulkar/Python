#Write a program with class as numbers and 
#four instance methods as ChkPrime(), ChkPerfect(),SumFactors(),Factors()
#accept input from user and call all instance methods using objects 


class Numbers :

    def __init__(self,Data):
        self.No = Data

    def ChkPrime(self):
        i = 0
        Flag = True
        for i in range (int(self.No/2) , 2 , -1):
            if (self.No % i ==0):
                Flag == False
                break

        return Flag


    def SumFactors(self):
        Sum = 0
        for i in range (1 ,int(self.No/2)+1):
            if (self.No%i == 0):
                Sum += i

        return Sum


    def ChkPerfect(self):
        Ans = self.SumFactors()

        if (self.No == Ans):
            return True

        else:
            return False




    
    def Factors(self):
        print("Factors of {} are :".format(self.No))
        for i in range (1 ,int(self.No/2)+1):
            if (self.No%i == 0):
                print(i)

def main():
    print("Please enter a Number")
    A = int(input())

    Obj = Numbers(A)
    ret = Obj.ChkPrime()
    if ret == True:
        print("{} is Prime ".format(A))
    else :
        print("{} is not Prime ".format(A))

    ret = Obj.ChkPerfect()
    if ret == True:
        print("{} is A perfect Number ".format(A))
    else:
        print("{} is A Not perfect Number ".format(A))

    Sum = Obj.SumFactors()
    print("Sum of Factors : ",Sum)

    Obj.Factors()


    




if __name__ == "__main__":
    main()