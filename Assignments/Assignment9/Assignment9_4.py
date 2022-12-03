import os
def Write_File(FileName,CopyFile):
    if(os.path.exists(CopyFile)):
        fr = open(CopyFile, 'r')

        fd = open(FileName , 'r')
        for lines in fd :
            for line in fr :
                if lines == line :
                    print("Files are same")
                    break
                else:
                    print("Lines are not same")

    else:
        print("File does not exist ")
        return


def main():
    print("Enter the file name to search : ")
    Name = input()
    print("Enter the file name to compare data from :")
    CopyFile = input()
    Write_File(Name,CopyFile)

if __name__ =="__main__":
    main()