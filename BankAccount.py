class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        after_depo_amount = amount + self.balance
        print(f'Amount deposited: ${amount}\n new balance: ${after_depo_amount}')
        return after_depo_amount

    def withdraw(self, amount):
        if self.balance > amount:
            after_wd_amount =self.balance - amount 
            print(f'Amount deposited: ${amount}\n new balance: ${after_wd_amount}')
        else:
            print(f'Insufficient funds. $10 overdraft fee has been charged to your account. Current Balance:{self.balance - 10 } ')

    def get_balance(self):
        print(f'Your balance is currently {self.balance}')
        return self.balance

    def add_interest(self, months):
        interest = months * 0.00083
        print(f'Current balance plus interest: {self.balance + interest}')
        
        #adds interest to balance
        #monthly interest (interest = balance *  0.00083 )
        pass
    
    def print_statement(self):
        num = self.account_number[4:8]
        print(f'{self.full_name}\nAccount No.: ****{num}\nBalance: ${self.balance}')
        #Joi Anderson
        #Account No.: ****5678
        #Balance: $100.00

testAccount = BankAccount("Rae Porhammer", "86753592", 37.90)
#testAccount.deposit(23.17)
#testAccount.withdraw(42)
#testAccount.withdraw(7.75)
#testAccount.get_balance()
#testAccount.add_interest(14)
testAccount.print_statement()

