import os
import multiprocessing


def Square(No):
    print("PID of Worker process is {} for the Input {}".format(os.getpid(),No))
    return (No**2)

def main():
    print("Process ID of our Application is : ",os.getpid())
    
    Data = [1,2,3,4,5]
    result = []

    Pobj = multiprocessing.Pool()
    result = Pobj.map(Square,Data)

    print("Result After Square Operation is : ",result)

if __name__ == "__main__":
    main()