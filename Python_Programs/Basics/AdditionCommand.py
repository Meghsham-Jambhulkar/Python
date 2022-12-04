import sys

def addition(A, B):
    ans = 0
    ans = A + B
    return ans

def main():
    if (len(sys.argv) != 3):
        print("Invalid Number of Arguments")

    ret = addition(int(sys.argv[1],int(sys.argv[2])))
    print("Addition is : ",ret)

if __name__ == "__main__":
    main()