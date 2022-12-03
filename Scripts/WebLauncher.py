from sys import *
import webbrowser
import re
import urllib

def is_connected():
    try: 
        urllib.request.urlopen('https://www.google.com')
        
    except Exception as err:
        return False

def Find(string):
    url = re.findall("((http|https)://)(www.)?"+"[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]"+"{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)", string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        lines = fp.readlines()
        for line in lines:
            print(line)
            url = Find(line)
            print(url)
            for urls in url:
                webbrowser.open(urls,new=2)




def main():
    print("----------Marvellous Infosystem Automations----------")

    print("Automation Script started with name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments ")
        print("Use -h for help and use -u for usage of script ")
        exit()
    elif(argv[1] == "-h" or argv[1]== "-H"):
        print("Help : This script is used to launch URL from text File ")
        exit()

    elif(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Provide 1 argument as text file as input")
        exit()
    #try :
        # connected = is_connected()
        # if connected:
    WebLauncher(argv[1])
        # else :
        #     print("Unable to connect to internet ")
    # except ValueError:
    #     print("Error : Invalid Datatype of Input ")
    # except Exception as E:
    #     print("Error : Invalid Input :",E)
        
if __name__ == "__main__":
    main()
