import time 
#serial with application execution time

def DisplayEven(No):
    for i in range(1,No+1):
        if( i % 2 == 0):
            print("Even Number :",i)




def DisplayOdd(No):
    for i in range(1,No+1):
        if( i % 2 != 0):
            print("Odd Number :",i)


def main():
    print("Demonstration of serial programming")
    DisplayEven(2000)
    print()
    DisplayOdd(2000)



if __name__ == "__main__":
    start_time = time.time()# calculate time like stopwatch 
    main()
    end_time = time.time()
    print("Execution time is : ",end_time - start_time)