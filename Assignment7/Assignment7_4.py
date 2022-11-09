#Check whether there are lowercase or uppercase or number in string 


import threading




def Small(str):
    Cnt1 = 0
    for i in str:
        if (i.islower()) == True:
            Cnt1 += 1

    print("Number of lowercase elements in string : ",Cnt1)



def Capital(str):
    Cnt2 = 0
    for i in str:
        if (i.isupper()) == True:
            Cnt2 += 1

    print("Number of Upper Case elements in string : ",Cnt2)
    


def Numbers(str):
    Cnt3 = 0
    for i in str:
        if (i.isdigit()) == True:
            Cnt3 += 1

    print("Number of Numeric elements in string : ",Cnt3)




def main():
    str = " Meghsham Jambhulkar PM401000300"
    t1 = threading.Thread(target= Small, args= (str,))
    t2 = threading.Thread(target= Capital , args= (str,))
    t3 = threading.Thread(target= Numbers , args= (str,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("End of Main")    

if __name__ == "__main__":
    main()