from sys import *

def Script_Task(No):
    if (No % 2 == 0):
        print("Number is Even")
    else :
        print("Number is Odd")


def main():
    print("----------Marvellous Infosystem Automations----------")

    print("Automation Script started with name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments ")
        print("Use -h for help and use -u for usage of script ")
        exit()
    elif(argv[1] == "-h" or argv[1]== "-H"):
        print("Help : This script is used to perform ________________")
        exit()

    elif(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Provide ___ number of arguments as ")
        print("First Argument as :______")
        print("Second Arguments as :_____")
        exit()
    else :
        Script_Task(int(argv[1]))
if __name__ == "__main__":
    main()
