#Write a program which contains one function that accept one number from user and 
#returns true if number is divisible by 5 otherwise false 

def main():
    print("Enter a number : ")
    no = int(input())

    if no % 5 == 0 :
        print("True")
    else :
        print("False")

if __name__ =="__main__":
    main()