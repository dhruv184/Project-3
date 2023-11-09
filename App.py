from Bank import Bank
from Saving_Checking import Saving_Account , CheckingAccount

class Application:

    def __init__(self , bank):
        self.bank = bank
        
    def run(self):

        while True:

            print("\n1. Create Account")
            print("2. Deposit Amount")
            print("3. WithDraw Amount")
            print("4. Get Balance")
            print("5. Apply Interest (Savings Account)")
            print("6. Exit\n")

            choice = input("Enter your Choise : ")

            if choice == "1":

                account_type = input("Enter Account Type [ 1 --> SAVINGS , 2 --> CHECKING ] : ")
                
                account_number = int(input("Enter Account Number : "))

                account_holder_name = str(input("Enter Account Holder Name : "))
                
                if account_type == "1":

                    interest_rate = float(input("Enter Interest Rate for Saving Account : "))
                    account = Saving_Account(account_number , account_holder_name , interest_rate)

                elif account_type == "2":

                    overdraft_limit = float(input("Enter OverDraft Limit for Checking Account : "))
                    account = CheckingAccount(account_number , account_holder_name , overdraft_limit)

                else:

                    print("\nInvalid Account Type\n")
                    continue

                self.bank.Add_Account(account)

                print(f"\nAccount : {account_number} Created\n")

            elif choice == "2":

                account_number = int(input("Enter Account Number : "))

                account = self.bank.get_Account(account_number)

                if account:

                    amount = float(input("Enter Deposit Amount : "))
                    print(account.Deposit(amount))

                else:

                    print("\nAccount not Found\n")

            elif choice == "3":

                account_number = int(input("Enter Account Number : "))

                account = self.bank.get_Account(account_number)

                if account:

                    amount = float(input("Enter WithDrawal Amount : "))
                    print(account.Withdraw(amount)) 

                else:

                    print("\nAccount not Found\n")                

            elif choice == "4":

                account_number = int(input("Enter Account Number : ")) 
                account = self.bank.get_Account(account_number)

                if isinstance(account ,Saving_Account):
                    print(account.apply_interest())

                else:

                    print("\nInvalid Account Type\n") 

            elif choice == "6":
                
                print("\nThanks for Visiting Bank\n")

                break

            else:

                print("\nInvalid choice. Please Try Again\n") 

bank = Bank()
app = Application()
app.run()