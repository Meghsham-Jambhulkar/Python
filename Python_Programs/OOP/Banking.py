#Creating a basic banking CLI containing 
#Instance Variable : Name , Amount , Address , AccountNo
#Class Variable : Bank_Name , ROI_On_FD
#Instance Method : CreateAccount() , DisplayAccountInfo()
#Class Method : DisplayACcountInformation
#Static Method : DisplayKYCInfo

import random

class Bank_Account :
    Bank_Name = "HDFC bank PVT LTD "
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name =""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = random.randint(101,999)
        self.Amount =  0

    def CreateAccount(self):
        print("Enter Name :")
        self.Name = input()

        print("Enter your initial Amount :")
        self.Amount = int(input())

        print("Enter Address :")
        self.Address = input()

        # print("Enter your Account No :")
        # self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("--------Your Account Information is as following--------")
        print("Name of Account Holder : ",self.Name)
        print("Account Number : ",self.AccountNo)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in Account : ",self.Amount)
    
    @classmethod
    def DisplayBankInformation(cls):
        print("----------Welcome to Banking Console----------")
        print("Name of our Bank is : ",cls.Bank_Name)
        print("Rate of intrest we offer on Fixed Deposit is : ",cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please Consider Below KYC information ")
        print("According to the rules of GOV of India You have to Submit Below Document ")
        print("1 : Clear and Recent Passport Size Photo")
        print("2 : Photo of aadhar Card")
        print("3 : Photo of PAN card")

    def Deposit(self,Value):

        self.Amount = self.Amount + Value

    
    def Withdraw(self,Value):
        self.Amount = self.Amount - Value


        
        

def main():
    print("-----------Banking Application----------")
    print("-------------------------------------------------------------")
    print("----------Calling Static Method to display KYC info----------")
    Bank_Account.DisplayKYCInfo()
    print("-------------------------------------------------------------")

    ("--------Calling Class Method to Display Account Information-------")
    Bank_Account.DisplayBankInformation()
    User1 = Bank_Account() 
    User2 = Bank_Account()
    print()
    print("--------Enter Account Information for First Account Holder--------")
    User1.CreateAccount()
    print()
    print("--------Enter Account Information for Second Account Holder--------")
    User2.CreateAccount()

    print("--------Calling Instance method to Display information of First Account Holder--------")
    User1.DisplayAccountInfo()
    print()
    print("--------Calling Instance method to Display information of Second Account Holder--------")
    User2.DisplayAccountInfo()
    print()

    User1.Deposit(500)
    User2.Deposit(1200)
    
    print("Amount of {} after Deposit is : {} " .format(User1.Name,User1.Amount))
    print("Amount of {} after Deposit is : {} " .format(User1.Name,User2.Amount))


    User1.Withdraw(200)
    User2.Withdraw(3000)

    
    print("Amount of {} after Withdrawl is : {} " .format(User1.Name,User1.Amount))
    print("Amount of {} after Wirhdrawl is : {} " .format(User1.Name,User2.Amount))

    print("--------End OF Banking Application--------")


if __name__ == "__main__":
    main()