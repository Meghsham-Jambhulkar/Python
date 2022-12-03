# Write a Program which accept one number from user and check whether its prime or not 
def ChkPrime(no):
    if no > 1 :
        for i in range ( 2, no):
            if (no % i)==0:
                print("It is not Prime Number")
                break
            else:
                print("It is Prime Number ")
                break

            


def main():
    print("Enter a number ")
    no = int(input())

    ChkPrime(no)

if __name__ == "__main__":
    main()

