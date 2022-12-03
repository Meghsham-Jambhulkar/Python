# display 1 to 50 by thread 1 and 50 to 1 by thread 2 and schedule thread 2 after thread 1 finishes

import threading 
def Display(No):
    for i in range(0,No):
        print (i)
        



def Reverse(No):
    for i in range(No , -1 , -1):
        print(i)








def main():
    N = 10
    t1 = threading.Thread(target= Display, args= (N,))
    t2 = threading.Thread(target= Reverse, args= (N,))

    t1.start()
    t1.join()
    print("****************************")
    t2.start()
    t2.join()

    print("End of main")






if __name__ == "__main__":
    main()