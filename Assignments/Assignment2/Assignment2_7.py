#Write a program which accept one number and display below pattern of number box 

def main():
    print("Enter a number : ")
    no = int(input())
    print("__________________________________")
    for i in range (1,no+1):
        for i in range (1,no+1 ):
            print(i, end=" ")
        print()
            
       

if __name__ == "__main__":
    main()