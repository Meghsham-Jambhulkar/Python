#Write a program which accept number from user and print that number of"*" on screen 

def main():
    print("Enter a number : ")
    no = int(input())

    print("_____________________________")
    
    while no > 0:
        print("*", end=" ")
        no -= 1

if __name__ == "__main__":
    main()