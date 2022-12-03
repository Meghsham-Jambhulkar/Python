#write a program which display 5 times marvellous on screen 
def main():
    print("Enter a word to repeat")
    w = input()

    print("___________________________")

    for i in range (0,5):
        print(w)

if __name__ == "__main__":
    main()
