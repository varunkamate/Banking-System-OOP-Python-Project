#Revision of the oop concepts
#Creating a banking system that contain method of deposite,withdraw and check balance


pass_word="123456"

class BankAccount:
    def __init__(self,acc_holder_name,balance=0):
        self.acc_holder_name=acc_holder_name
        self.balance=balance

    def diposite(self,ammount):
        pin=input("Enter the account holder pass word here: ")
        if pin==pass_word:
            if ammount>0:
                self.balance+=ammount
                print(f"Your total balance  is {self.balance}")
                print("Thank you 🙏🙂")
            else:
                print("Please enter the positive amount")
        else:
            print("Wrong password❌❌❌")
    
    def withdraw(self,ammount):
        pin=input("Enter the account holder pass word here: ")
        if pin==pass_word:
            if ammount>self.balance:
                print("Insufficient balance❌❌❌")
            elif ammount<self.balance:
                print(f"Here is your withdraw amount {ammount}")
                self.balance-=ammount
                print(f"Remaining balance is {self.balance}")
            else:
                print("Please enter the valid amount")
        else:
            print("Invalid pass word")
        
    def check_balance(self):
        pin=input("Enter the password here: ")
        if pin==pass_word:
            print(f"Hi {self.acc_holder_name}")
            print(f"Here is your total balance: {self.balance}")
            print("Thank you for choosing us🙏🙏🙂")
        else:
            print("Invalid pin please enter the valid pin")
        


#Banking System Usage Here

def app():
    print("🤚 Hi welcome to Krishna bank😊😊😊")
    name=input("Enter your name here: ")
    account=BankAccount(name)

    while True:
        print("Choose options among:")
        print("1 - (Diposite)")
        print("2 - (Withdraw)")
        print("3 - (Check Balance)")
        print("4 - (Exit or Quite)")

        choice=input("Enter your choice here: ")

        if choice=="1":
            ammount=float(input("Enter the amount here: "))
            account.diposite(ammount)
        elif choice=="2":
            ammount=float(input("Enter the amount here: "))
            account.withdraw(ammount)
        elif choice=="3":
            account.check_balance()
        elif choice=="4":
            print("Thankyou for using Krishna bank🙏🙏😊")
            break
        else:
            print("Please enter the valid option")
        
if __name__ == "__main__":
    app()
