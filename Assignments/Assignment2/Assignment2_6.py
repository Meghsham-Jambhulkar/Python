#Write a program which accept a number and display pattern

def main():
    print("Enter a number ")
    no = int(input())
    print("__________________________________")
    for i in range(no,0,-1):
        for i in range(0,i):
            print("*" , end=" ")
        print()

if __name__ == "__main__":
    main()     