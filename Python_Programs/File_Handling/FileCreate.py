import os

def FileCreate(FileName):
    if(os.path.exists(FileName)):
        print("File Already Exists")
        return
    else:
        fd = open(FileName,"w")


def main():
    print("Enter the file name to create : ")
    Name = input()
    FileCreate(Name)




if __name__ =="__main__":
    main()