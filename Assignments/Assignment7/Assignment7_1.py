#Design Python application which creates two thread named as even and odd . 
#Even Thread will display first 10 even numbers and first 10 odd numbers

import threading 
def DisplayEven(No):
    for i in range(1,No+1):
        if( i % 2 == 0):
            print("Even Number :",i)



def DisplayOdd(No):
    for i in range(1,No+1):
        if( i % 2 != 0):
            print("Odd Number :",i)








def main():
    N = 10
    t1 = threading.Thread(target= DisplayEven, args= (N,))
    t2 = threading.Thread(target= DisplayOdd, args= (N,))

    t1.start()
    t2.start()






if __name__ == "__main__":
    main()