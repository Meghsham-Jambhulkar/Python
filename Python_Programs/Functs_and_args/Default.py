
def Area(Radius , PI = 3.14):
    Result = PI * Radius * Radius
    return Result

def main():
    RValue = 10.5
    PIvalue = 3.14

    ans = Area(RValue,PIvalue) #ans = Area(10.5,3.14) positional arguments
    print("Area of Circle is : ",ans)

    ans = Area(Radius = RValue ,PI = PIvalue) #ans = Area(10.5,3.14) keyword arguments
    print("Area of Circle is : ",ans)

    #Positional and Default arguments
    ans = Area(10.5) #ans = Area(10.5) 
    print("Area of Circle is : ",ans)

    #Keyword and Default argument 
    ans = Area(Radius = 10.5) #ans = Area(10.5)
    print("Area of Circle is : ",ans)

    #keword argument 
    ans = Area(PI = 7.10,Radius = 10.5) #ans = Area(7.10,10.5)
    print("Area of Circle is : ",ans)

if __name__ == "__main__":
    main()

#346.185