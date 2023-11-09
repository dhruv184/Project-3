class Account:

    def __init__(self , account_number , account_Holder_Name , current_Balance):

        self.account_number = account_number
        self.account_Holder_Name = account_Holder_Name
        self.current_Balance = current_Balance

    def get_Account_Number(self):

        return f"Account Number is {self.account_number}"    
    
    def get_Account_Holder_Name(self):

        return f"Account Holder Name is {self.account_Holder_Name}"
    
    def get_Balance(self):

        return f"Current Balance is {self.current_Balance}"
    
    def Deposit( self , amount) :

        self.current_Balance +=amount
        return f"Deposited amount : {amount}. New Balance is {self.current_Balance}"
    
    def Withdraw( self , amount ): 

        if self.current_Balance >= amount:

            self.current_Balance -= amount
            return f"Withdrawal amount : {amount}. New Balance is {self.current_Balance}"
        
        else:

            return "Insufficient Funds"
