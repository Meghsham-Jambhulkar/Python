#Write a program with class arithmatic 
#and 5 methods called accept ,addition, substraction, multipication and division 

class Arithmetic  :
    
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.sum = 0
        self.sub = 0
        self.mult = 0
        self .div = 0


    def Accept(self):
        print("Enter First Number : ")
        self.value1 = int(input())
        print()
        print("Enter Second  Number : ")
        self.value2 = int(input())

    def Addition(self):
        self.sum = self.value1 + self.value2
        print("Addition of two number {} and {} is {}  ".format(self.value1,self.value2,self.sum))


    def Substraction(self):
        self.sub = self.value1 - self.value2
        print("Substraction of two number {} and {} is {}  ".format(self.value1,self.value2,self.sub))

    def Multiplication(self):
        self.mult = self.value1 * self.value2
        print("Multiplication of two number {} and {} is {}  ".format(self.value1,self.value2,self.mult))

    def Division(self):
        self.div = self.value1 / self.value2
        print("Division of two number {} and {} is {}  ".format(self.value1,self.value2,self.div))

def main():
    obj = Arithmetic()

    obj.Accept()
    obj.Addition()
    obj.Substraction()
    obj.Multiplication()
    obj.Division()





if __name__ =="__main__":
    main()