def main():

    Batches = { "PPA": 18000 ,"LB":16700,"Python":16500,"Angular":15000}
    print("Data of Dictonary : ", Batches)

    print("Data traversal using for Loop ")
    for x in Batches:
        print(x)
    
    print("________________________________")
    

    print("Data traversal using for Loop ")
    for x in Batches:
        print(x,Batches[x])
    print("________________________________")
    
    print("Data traversal using for Loop ")
    for x in Batches:
        print(x,Batches.get(x))
    print("________________________________")
    
    
    keyBatches = Batches.keys()
    valueBatches = Batches.values()
    print(type(keyBatches))
    print(keyBatches)
    print(type(valueBatches))
    print(valueBatches)

if __name__ =="__main__":
    main()