class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        after_depo_amount = amount + self.balance
        print(f'Amount deposited: ${amount}\n new balance: ${after_depo_amount}')
        return after_depo_amount
        #adds amount to balance
        #“Amount deposited: $X.XX new balance: $Y.YY”

    def withdraw(self, amount):
        if self.balance > amount:
            after_wd_amount =self.balance - amount 
            print(f'Amount deposited: ${amount}\n new balance: ${after_wd_amount}')
        else:
            print(f'Insufficient funds. $10 overdraft fee has been charged to your account. Current Balance:{self.balance - 10 } ')
        #subtracts amount from balance
        #“Amount withdrawn: $X.XX new balance: $Y.YY”
        #user tries to withdraw an amount greater than balance, ”Insufficient funds.”
        #overdraft fee ($10)
        pass

    def get_balance(self):
        print(f'Your balance is currently {self.balance}')
        return self.balance

    def add_interest(self, months):

        #adds interest to balance
        #monthly interest (interest = balance *  0.00083 )
        pass
    
    def print_statement(self):
        #Joi Anderson
        #Account No.: ****5678
        #Balance: $100.00
        pass

testAccount = BankAccount("Rae Porhammer", 86753090, 37.90)
#testAccount.deposit(23.17)
#testAccount.withdraw(42)
testAccount.withdraw(7.75)