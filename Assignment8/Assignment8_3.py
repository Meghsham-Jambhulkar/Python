def Numbers(No):
    Cnt = 0
    if (No > Cnt):
        print(No,end=" ")
        No -=1 
        Numbers(No)

def main():
    print("Enter number :")
    No = int(input())
    Numbers(No)
    



if __name__ == "__main__":
    main()