#Design python applicaton which creates two as evenlist and oddlist .
#both threads accept list of integers as parameters evenlist thread will add all even numbers from input list
#and display addition and odd list will add all odd elements from input list and display addition

import threading


def Evenlist(No):
    sum = 0
    for i in No:
        if( i % 2 == 0):
            sum += i 

    print("Sum of Even:",sum)


def Oddlist(No):
    sum = 0
    for i in No:
        if( i % 2 != 0):
            sum += i 

    print("Sum of Odd :",sum)

def main():
    N = [10,9,8,7,6,5,4,3,2,1]
    t1 = threading.Thread(target= Evenlist, args= (N,))
    t2 = threading.Thread(target= Oddlist , args= (N,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of Main")    

if __name__ == "__main__":
    main()