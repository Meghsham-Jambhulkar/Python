import os 

def CheckFile(Fname):
    if(os.path.exists(Fname)):
        print("File Exists")
    else:
        print("File does not exist ")
        return
def main():
    print("Enter the file name : ")
    Name = input()
    CheckFile(Name)

if __name__ == "__main__":
    main()