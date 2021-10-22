class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        #adds amount to balance
        #“Amount deposited: $X.XX new balance: $Y.YY”
        pass

    def withdraw(self, amount):
        #subtracts amount from balance
        #“Amount withdrawn: $X.XX new balance: $Y.YY”
        #user tries to withdraw an amount greater than balance, ”Insufficient funds.”
        #overdraft fee ($10)
        pass

    def get_balance(self):
        print(f'Your balance is currently {self.balance}')
        return self.balance

    def add_interest(self):
        #adds interest to balance
        #monthly interest (interest = balance *  0.00083 )
        pass
    
    def print_statement(self):
        #Joi Anderson
        #Account No.: ****5678
        #Balance: $100.00
        pass
    