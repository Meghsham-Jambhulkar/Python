#Function which accepts nothing and returns nothing
from traceback import print_tb


def Demo1():
    print("Inside Demo1 ")

#Function accepts one parameter and returns nothing 
def Demo2(No):
    print("Inside Demo2 with Argument :",No)
    
#Function accepts one parameter and return 1 parameter 
def Demo3(No):
    print("Inside Demo3 with argument : ",No)
    return No+2

#Function accepts two parameters and return one parameter
def Demo4(No1, No2):
    print("Inside Demo4 with arguments :",No1,No2)
    add = No1 + No2
    return add
#Function accepts two parameters and return one parameter 
def Demo5(No1, No2):
    print("Inside Demo5 with arguments :",No1,No2)
    add = No1 + No2
    sub = No1 - No2
    return add , sub

def main():
    Demo1()
    Demo2(11)
    ans = Demo3(10)
    print("Return Value of Demo3 is : " , ans)
    ans = Demo4(10,11)
    print("Return value of Demo4 is : ",ans)
    ans1 , ans2 = Demo5(11,10)
    print("First Return value of Demo5 is : ",ans1)
    print("Second Return value of Demo5 is : ",ans2)

if __name__ == "__main__":
    main()