
import random

class Bank_Account :
    Bank_Name = "Marvellous Bank"
    ROI_On_FD = 10.7

    def __init__(self):
        self.Name = "Meghsham"
        self.Amount = 0
        self.AccountNo = random.randint(101,999)
       
    def Display(self):
        print("--------Your Account Information is as following--------")
        print("Name of Account Holder : ",self.Name)
        print("Account Number : ",self.AccountNo)
        print("Current Amount in Account : ",self.Amount)
    
    @classmethod
    def DisplayBankInformation(cls):
        print("----------Welcome to Banking Console----------")
        print("Name of our Bank is : ",cls.Bank_Name)
        print("Rate of intrest we offer on Fixed Deposit is : ",cls.ROI_On_FD)

    def Deposit(self,Value):

        self.Amount = self.Amount + Value

    
    def Withdraw(self,Value):
        self.Amount = self.Amount - Value

    def CalculateROI(self , Value ):
        self.Amount = self.Amount * (Bank_Account.ROI_On_FD/10)

        
        

def main():
    print("-----------Banking Application----------")

    User1 = Bank_Account()
    print()
    User1.Display()
    print()

    User1.Deposit(500)
    print("Amount of {} after Deposit is : {} " .format(User1.Name,User1.Amount))

    User1.Withdraw(200)
    print("Amount of {} after Withdrawl is : {} " .format(User1.Name,User1.Amount))

    User1.CalculateROI(500)
    print("Rate of Intrest is : {} " .format(User1.Amount))

    print("--------End OF Banking Application--------")


if __name__ == "__main__":
    main()