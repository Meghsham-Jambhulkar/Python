import os
def Write_File(FileName,CopyFile):
    if(os.path.exists(CopyFile)):
        fr = open(CopyFile, 'r')

        fd = open(FileName , 'w')
        for line in fr:
            fd.write(line)

    else:
        print("File does not exist ")
        return


def main():
    print("Enter the file name to create : ")
    Name = input()
    print("Enter the file name to copy data from :")
    CopyFile = input()
    Write_File(Name,CopyFile)

if __name__ =="__main__":
    main()