import os
from sys import *

def Directory_Watcher(Path):
    print("----------Inside Directory Watcher Method ----------")
    print("Name of input directory : ",Path)

    flag = os.path.isabs(Path)
    if flag == False:
        path = os.path.abspath(Path)

    exists = os.path.isdir(Path)

    if exists:
        for foldername, subfolder, Filename in os.walk(Path):
            print("Folder name is : "+foldername)
            for subf in subfolder:
                print("Subfolder name of "+foldername+" is "+subf)
            for fnames in Filename:
                print("File inside folder "+foldername+" is "+fnames)
                print("With Size :",os.path.getsize(os.path.join(foldername,fnames)))
            print("--------------------------------------------------")

def main():
    print("----------Directory watcher application----------")

    if(len(argv) != 2):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    try:
        Directory_Watcher(argv[1])
    
    except ValueError:
        print("Error : Invalid Datatype of Input")
    
    except Exception:
        print("Error : Invalid Input ")


if(__name__ =="__main__"):
    main()