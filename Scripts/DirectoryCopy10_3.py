import os
from sys import *
import shutil

def Directory_Watcher(path):
    print("----------Inside Directory Watcher Method ----------")
    print("Name of input directory : ",path)

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)


    for foldername, subfolder, filename in os.walk(path):
        for fnames in filename :
            if fnames.lower().endswith(extension):
                print("hi")

def Foldercreator(des_dir,log_dir = "Marvellous"):
        src_dir = argv[2]
        des_dir = argv[1]
        if not os.path.exists(log_dir):
            try:
                os.mkdir(log_dir)
            except:
                pass    
        else : 
            shutil.copytree(src_dir, des_dir)
                
    

def main():
    print("----------Directory watcher application----------")
    print("Name of the application : ",argv[0])



    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    if(len(argv) != 3):
        print("Insufficient arguments")
        print(len(argv))
        exit()

    Foldercreator(argv[2],argv[1])
if(__name__ =="__main__"):
    main()