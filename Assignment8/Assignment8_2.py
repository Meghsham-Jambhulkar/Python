def Numbers(No):
    Cnt = 1
    while (Cnt < No):
        print(Cnt,end=" ")
        Cnt += 1 
        Numbers(No)

def main():
    print("Enter number :")
    No = int(input())
    Numbers(No)
    



if __name__ == "__main__":
    main()