import os

def DeleteFile(FileName):
    if(os.path.exists(FileName)):
        
        size = os.path.getsize(FileName)
        if size == 0:
            os.remove(FileName)
            print("File {} Deleted Succesfully".format(FileName))
        else:
            print("Are you sure file needs to be deleted Y/N")
            opt = input()
            if(opt == "Y"or opt =="y"):
                os.remove(FileName)
                print("File {} Deleted Succesfully".format(FileName))
        
            else: 
                print("File Deletion Aborted")

    else:
        print("File Does not exist....")
        return


def main():
    print("Enter the file name to create : ")
    Name = input()
    DeleteFile(Name)




if __name__ =="__main__":
    main()