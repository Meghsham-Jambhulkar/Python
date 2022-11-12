def PatternP(No):
    Cnt = 0
    if (No > Cnt):
        print("*",end=" ")
        No -= 1
        PatternP(No)

def main():
    print("Enter number :")
    No = int(input())
    PatternP(No)
    



if __name__ == "__main__":
    main()