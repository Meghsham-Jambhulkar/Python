#Write A program to display class as circle Three instance variable 
#one class variable as PI Write Four instance method  Accept CalculateArea , CalculateCircumference ,Display





class Circle :
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        print("Enter radius of a circle : ")
        self.Radius = float(input())

    def Area(self):
        self.area = Circle.PI * self.Radius * self.Radius
        print("Area of Circle is with radius {} is {}  ".format(self.Radius,self.area))


    def Circumference(self):
        self.circumference = 2 * Circle.PI * self.Radius
        print("Circumference of Circle is with radius {} is {}  ".format(self.Radius,self.circumference))

def main():
    obj = Circle()

    obj.Accept()
    obj.Area()
    obj.Circumference()





if __name__ =="__main__":
    main()