#Accept Two numbers and perform addition and substraction of it 
#Class = Characteristics + Behaviours
#Class = Data + Functions 


class Arithmatic:
    def __init__ (self,A,B) :
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1+self.No2

    def Sub(self):
        return self.No1-self.No2

    
def main():
    print("Enter First Number : ")
    Value1 =  int(input())

    print("Enter Second Number : ")
    Value2 =  int(input())

    obj = Arithmatic(Value1,Value2)
    print("Type of Object is : ",type(obj))
    Ans = obj.Add()
    print("Addition is :",Ans)

    Ans =obj.Sub()
    print("Substraction is :",Ans)




if __name__ == "__main__":
    main()