#Write a program which accept one number fromuser and returns additions of its factors 

from traceback import print_tb


def main():
    print("Enter a number : ")
    no = int(input())
    res = 0
    i = 1
    print("_____________________________")
    for i in range(1,no):
        if no%i==0 :
            res = res + i
    print("The sum of Factors are " ,res)
            

           
        

if __name__ == "__main__":
    main()