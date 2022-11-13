import os
def Write_File(FileName):
    if(os.path.exists(FileName)):
        fd = open(FileName , "r")
        Data = fd.read()
        print("Data from File is :")
        print(Data)
        fd.close()

    else:
        print("File does not exist ")
        return

def main():
    print("Enter the file name : ")
    Name = input()
    Write_File(Name)

if __name__ =="__main__":
    main()