#Write a program which accepts numbers from user and returns addition of digits in that number     
def main():
    print("Enter a number :")
    no = int(input())
    ans = list(no)
    print("The Length of the input number is  : ",sum(ans))


if __name__ == "__main__":
    main()