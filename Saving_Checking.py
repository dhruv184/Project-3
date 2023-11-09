from Account import Account

class Saving_Account(Account):

    def __init__(self , account_number , account_Holder_Name , interest_rate , current_Balance = 0):

        super().__init__(account_number , account_Holder_Name , current_Balance )
        self.interset_rate = interest_rate

    def apply_interest(self):

        Interest_Amount = self.current_Balance * self.interset_rate
        self.current_Balance += Interest_Amount

        return f"Interest applied amount : {Interest_Amount}. New Balance is {self.current_Balance}"

class CheckingAccount(Account):

    def __init__(self ,account_number , account_Holder_Name , overdraft_limit  , current_Balance = 0):        

        super().__init__(account_number , account_Holder_Name , current_Balance)
        self.overdraft_limit = overdraft_limit

    def Withdraw(self, amount):

        if self.current_Balance + self.overdraft_limit >= amount:

            self.current_Balance -= amount
            return f"Withdrawal amount : {amount}. New Balance is {self.current_Balance}"

        else:

            return "Insufficient Funds"   