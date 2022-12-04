
def Square(No):
    return (No**2)

def main():
    Data = [1,2,3,4,5]

    result = []

    for Value in Data :
        result.append(Square(Value))

    print("Result After Square Operation is : ",result)

if __name__ == "__main__":
    main()