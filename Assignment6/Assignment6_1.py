#Write a program which contains one class BookStore with class variable NoofBooks  
#and two instance variable as Name and Author 
#There is one instance method of class as Display which displays name and author and number of books 

class BookStore :
    NoofBooks = 0
    def __init__(self):
        self.Name =""
        self.Author = ""
        BookStore.NoofBooks += 1

    def Display(self,Value1,Value2):
        print("{} by {}, Number of books {} ".format(Value1,Value2,BookStore.NoofBooks))

        

        


def main():
    obj1 = BookStore()
    obj1.Display("Linux System Progreamming","Robert Love")

    obj1 = BookStore()
    obj1.Display("C Progreamming","Dennies Richie")



if __name__ == "__main__":
    main()