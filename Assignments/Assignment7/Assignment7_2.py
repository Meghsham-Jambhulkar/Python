#Design Python Applicatoon which creates two threads as evenfactor and odd factor 
#Both the thread accept one parameter as integer. Even factor will generate addition of even factors 
#And Oddfactors will display addition of odd factors of given number adter exectution the both the threads get completed 
# main thread should display message as "exit from main"
import threading


def Evenfactor(No):
    sum = 0
    for i in range(No , 1 , -1):
        if( i % 2 == 0):
            sum += i 

    print("Sum of Even Factors :",sum)


def Oddfactor(No):
    sum = 0
    for i in range(No , 0 , -1):
        if( i % 2 != 0):
            sum += i 

    print("Sum of Odd Factors :",sum)

def main():
    N = 10
    t1 = threading.Thread(target= Evenfactor, args= (N,))
    t2 = threading.Thread(target= Oddfactor , args= (N,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of Main")    

if __name__ == "__main__":
    main()