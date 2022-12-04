
class Arithmatic :
    
    def __init__(self,A,B):#Special
        print("Inside Init Method")
        self.No1 = A
        self.No2 = B


    def Addition(self):
        Ans = self.No1+self.No2
        return Ans

    def Substraction(self):
        Ans = self.No1-self.No2
        return Ans
         


def main():

    print("Inside Main Method")

    obj = Arithmatic(11,10)
    output = obj.Addition()
    print("Addition is : ",output)
    output = obj.Substraction()
    print("Addition is : ",output)




if __name__ =="__main__":
    print("Inside Starter")
    main()