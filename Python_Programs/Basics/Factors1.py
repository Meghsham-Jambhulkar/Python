def main():
    print("Enter number ")
    no = int(input())
    print("Factors are : ")
    for i in range (1,no):
        if no % i == 0:
            print(i)





if __name__ == "__main__":
    main()