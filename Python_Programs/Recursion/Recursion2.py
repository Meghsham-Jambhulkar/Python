import sys


sys.setrecursionlimit(3001)

print(sys.getrecursionlimit())

def Display(No):
    Cnt = 0
    while(Cnt < No):
        print("Hello")
        Cnt +=  1
        Display(No)
    

Display(4)