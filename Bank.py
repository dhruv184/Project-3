class Bank:

    def __init__(self):

        self.accounts = [ ]

    def Add_Account(self,account):

        self.accounts.append(account)

    def get_Account(self, account_number):

        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None 

    def set_bank_name(self , bank_name):

        self.bank_name = bank_name

    def get_bank_name(self):

        return self.bank_name             