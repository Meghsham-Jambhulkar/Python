#Write a program which contains one class 
#two instance variable and one class variable as value 
#and two methods which displays values of instance variable 


class Demo:
    def __init__(self,A,B) :
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print()
        print("Values of First Instance Variable From Fun : ",self.no1)
        print("Values of Second Instance Variable From Fun: ",self.no2)


    def Gun(self):
        print()
        print("Values of First Instance Variable From Gun : ",self.no1)
        print("Values of Second Instance Variable From Gun: ",self.no2)




def main():
    Obj1 = Demo(11,51)
    Obj2 = Demo(51,101) 

    Obj1.Fun()
    Obj1.Gun()
    Obj2.Fun()
    Obj2.Gun()



    



if __name__ =="__main__":
    main()