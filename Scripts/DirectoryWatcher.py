#It is an automation script which displays current Process on console
import os
from sys import *

def Directory_Watcher(path):
    print("----------Inside Directory Watcher Method ----------")
    print("Name of input directory : ",path)

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)


    for foldername, subfolder, filename in os.walk(path):
        print("Folder name is : "+foldername)
        for subf in subfolder:
            print("Subfolder name of "+foldername+" is "+subf)
        for fnames in Filename:
            print("File inside folder "+foldername+" is "+fnames)
        print("--------------------------------------------------")

def main():
    print("Directory watcher application")

    if(len(argv) < 2):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    Directory_Watcher(argv[1])
if(__name__ =="__main__"):
    main()