import os

def main():
    print("PID of Current Process is : ",os.getpid())
    print("PID of Parent Process is : ",os.getppid())

if __name__ == "__main__":
    main()