import os
def Write_File(FileName):
    if(os.path.exists(FileName)):
        print("Enter the Data that you want to write in the file")
        Data = input()

        fd = open(FileName , "a")
        fd.write(Data+"\n")

    else:
        print("File does not exist ")
        return


def main():
    print("Enter the file name to create : ")
    Name = input()
    Write_File(Name)

if __name__ =="__main__":
    main()