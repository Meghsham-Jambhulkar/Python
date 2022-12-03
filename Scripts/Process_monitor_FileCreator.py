#It is an autoomation script which displays Process and its memory usage on a log file
import os
import psutil
import time
from sys import *
import datetime


def ProcessDisplay(log_dir = "Marvellous"):
    listProcess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    separator = "-" * 30
    log_path = os.path.join(log_dir,"ProcessLog%s.csv"%(time.time()))
    f = open(log_path,'w')
    f.write(separator+"\n")
    f.write("Process Logger :"+time.ctime()+"\n")
    f.write(separator+"\n")

    for proc in psutil.process_iter():
        try : 
            pinfo = proc.as_dict(attrs=["pid","name","username"])
            pinfo['vms'] = proc.memory_info().vms/(1024*1024)
            # pinfo['vms'] = vms
            listProcess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    for element in listProcess:
        f.write("%s\n"%element)



def main():
    print("Script to Monitor Processes and Create Log File")
    print("----------Process Log----------")
    
    print("Automation Script started with name : "+argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments ")
        print("Use -h for help and use -u for usage of script ")
        exit()
    elif(argv[1] == "-h" or argv[1]== "-H"):
        print("Help : This script is used to record running process")
        exit()

    elif(argv[1] == "-u" or argv[1] == "-U"):
        print(("usage : Provide Absolute path of the Directory"))
        exit()

    ProcessDisplay(argv[1])
        
    # except ValueError:
    #     print("Error : Invalid Datatype of input")

    # except Exception:
    #     print("Error : Invalid Input")


if __name__ =="__main__":
    main()