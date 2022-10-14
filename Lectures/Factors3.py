def main():
    print("Enter number ")
    no = int(input())
    print("Factors are : ")
    i = 1
    while (i <= int(no/2)):
        if (no % i == 0): 
            print(i)
        i += 1 





if __name__ == "__main__":
    main()