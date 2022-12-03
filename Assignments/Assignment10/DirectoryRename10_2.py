import os
from sys import *

def Directory_Watcher(path,extension1,extension2):
    print("----------Inside Directory Watcher Method ----------")
    print("Name of input directory : ",path)

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)


    for foldername, subfolder, filename in os.walk(path):
        for fnames in filename :
            if fnames.lower().endswith(extension1):
                os.rename(extension1, extension2)
        

def main():
    print("----------Directory watcher application----------")


    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    # if(len(argv) != 4):
    #     print("Insufficient arguments")
    #     exit()

    Directory_Watcher(argv[1],argv[2],argv[3])
if(__name__ =="__main__"):
    main()