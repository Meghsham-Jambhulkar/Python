#Write a program which accept one number from user and return its factorial 

def main():
    print("Enter a number :")
    no = int(input())
    fact = 1
    for i in range(1,no+1 , 1):
        fact = fact * i

    print("The factorial of number",no,"is :",fact)

if __name__ == "__main__":
    main()
