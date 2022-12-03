# Write a program which contains one function named as ChkNum() \
# Which accept one parameter as number If number is even it should display "Even Number "
# otherwise display "Odd Number " on Console
#  
def chknum(no):
    if (no % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number ")

def main():
    print("Enter a number to Check number :")
    no = int(input())
    chknum(no)

if __name__ == "__main__":
    main()