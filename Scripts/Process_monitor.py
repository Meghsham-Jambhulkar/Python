import psutil


def ProcessDisplay():
    listProcess = []

    for proc in psutil.process_iter():
        try : 
            pinfo = proc.as_dict(attrs=["pid","name","username"])

            listProcess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listProcess

def main():
    print("----------Process Log Display----------")
    listprocess = ProcessDisplay()

    for elem in listprocess:
        print(elem)

if __name__ =="__main__":
    main()