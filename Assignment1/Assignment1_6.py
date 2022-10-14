#write a program which accept number from user 
#and check whether that number is positive or negative or zero

def main():
    print("Enter a number :")
    no = int(input())

    if no> 0 :
        print("Positive Number ")
    elif no < 0:
        print("Negative Number ")
    else:
        print("Zero ")

if __name__ ==  "__main__":
    main()