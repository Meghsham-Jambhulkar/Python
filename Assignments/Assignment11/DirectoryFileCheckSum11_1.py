import os
from sys import *
import hashlib


def hashfile(path , blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def DisplayChecksum(path):
    print("----------Inside Directory Watcher Method ----------")
    print("Name of input directory : ",path)

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:

        for foldername, subfolder, filename in os.walk(path):
            print("Current Folder is "+foldername)
            for fnames in filename :
                path = os.path.join(foldername,fnames)
                file_hash = hashfile(path)
                print("File Name and Path is ",path)
                print("Checksum or MD of file is ",file_hash)
            print("--------------------------------------------------")

def main():
    print("----------Directory CheckSum reader--------")


    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    if(len(argv) != 2):
        print("Insufficient arguments")
        exit()

    DisplayChecksum(argv[1])
if(__name__ =="__main__"):
    main()