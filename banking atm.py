class bank_account():
    def __init__(self):
        self.aomunt=0
    def depsite(self,Amount):
        self.amount+=Amount
        print("Amount Successfully Deposited")
    def withdraw(self,Amount):
        if(self.amount-Amount>=500):
            self.amount-=Amount
            print("Amount Successfully Withdrawn")
        else:
            print("Insufficient Balance.\nYou have to atleast .500LRD in your Account")
    def display(self):
        print("Your Bank Balance is",self.amount)

a=bank_account()
for i in range(0,50):
    print("1.Deposite 2.Withdraw 3.Display 4.Exit")
    p=int(input("Enter Your Choice:"))
    if(p==1):
        Amount=float(input("Enter Amount to be Deposite:"))
        a.deposite(Amount)
    elif(p==2):
        Amount=float(input("Enter Amount to be Withdrawn:"))
        a.withdraw(Amount) 
    elif(p==3):
        a.display()
    elif(p==4):
        exit()
    else:
        
        
        print("You have Enter a Wrong Value")    