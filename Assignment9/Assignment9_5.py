import os
def Write_File(FileName,srch):
    
    if(os.path.exists(FileName)):
        fd = open(FileName , 'r')
        data = fd.read()
        cnt = data.count(srch)
        return cnt

    else:
        print("File does not exist ")
        return


def main():
    print("Enter the file name to search : ")
    Name = input()
    print("Word to Search : ")
    srch = input()
    Ans = Write_File(Name,srch)
    print("Count of {} in {} is {}".format(srch,Name,Ans))
if __name__ =="__main__":
    main()