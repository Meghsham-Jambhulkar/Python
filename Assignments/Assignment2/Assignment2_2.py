#Write a program which accept one number and display below pattern 

def main():
    print("Enter a number : ")
    no1 = int(input())
    print("__________________________________")
    for i in range (no1):
        for i in range (no1):
            print("*", end=" ")
        print()
            
       

if __name__ == "__main__":
    main()