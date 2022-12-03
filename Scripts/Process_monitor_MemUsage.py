#It is an autoomation script which displays Process and its memory usage on console
import psutil


def ProcessDisplay():
    listProcess = []

    for proc in psutil.process_iter():
        try : 
            pinfo = proc.as_dict(attrs=["pid","name","username"])
            pinfo['vms'] = proc.memory_info().vms/(1024*1024)

            listProcess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listProcess

def main():
    print("----------Process Log Display With Memory info ----------")
    listprocess = ProcessDisplay()

    for elem in listprocess:
        print(elem)

if __name__ =="__main__":
    main()