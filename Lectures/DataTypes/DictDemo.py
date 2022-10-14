from cv2 import sort


def main():
    print("Demonstration of Dictonary")

    # Data : Heterogeneous
    # Ordered : Yes
    # Indexed : No
    # Mutable : Yes
    # Duplicates : Keys cannot be Duplicate
    #kenth thompson
    #linus stonewalon

    programming = { "C":"Ritchie ","C++":"Stroustrup", "Python ":"Rossum ","Java ": "Gosling ","C":"Thompson"}

    Batches = { "PPA": 18000 ,"LB":16700,"Python":16500,"Angular":15000}
    print("Data of Dictonary : ", programming)
    print("Data type is : ", type(Batches))
    print("Length Of Dictonary : ",len(Batches))
    print("Value of PPA is : ",Batches["PPA"])
    print("Sorted Batches Dictonary with key : ",sorted(Batches))
    print("Sorted Batches Dictonary with Values : ",sorted(Batches))



if __name__ == "__main__":
    main()