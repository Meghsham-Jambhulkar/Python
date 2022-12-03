#write a program which display 10 to 1 on screen
def main():
    print("Enter a number : ")
    no = int(input())
    print("__________________________")
    while no>0:
        print(no,end=" ")
        no -=1

if __name__ =="__main__":
    main()
