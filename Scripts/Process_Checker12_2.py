import psutil
from sys import *


def ProcessDisplay(procname):

    for proc in psutil.process_iter():
        try : 
            if procname.lower() in proc.name().lower():
                print(argv[1],"Process Exist in Monitor")
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

def main():
    print("----------Process Log Display----------")
    listprocess = ProcessDisplay(argv[1])


if __name__ =="__main__":
    main()