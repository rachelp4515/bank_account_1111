class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        print(f'Amount deposited: ${amount}\nNew balance: ${self.balance}')
        return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount 
            print(f'Amount withdrawn: ${amount}\nNew balance: ${self.balance}')
        else:
            print(f'Insufficient funds. $10 overdraft fee has been charged to your account. Current Balance:{self.balance - 10 } ')

    def get_balance(self):
        print(f'Your balance is currently {self.balance}')
        return self.balance

    def add_interest(self, months):
        interest = months * 0.00083
        self.balance += int((interest * self.balance * 100) + .5) / 100 #rounds to nearest hundreth. hundredth? hundrethd. its more complicated than it needs to be i know
        print(f'Current balance plus interest: {self.balance}')
        
        #adds interest to balance
    
    def print_statement(self):
        num = self.account_number[4:8]
        print(f'{self.full_name}\nAccount No.: ****{num}\nBalance: ${self.balance}')
        #Joi Anderson
        #Account No.: ****5678
        #Balance: $100.00

#testAccount = BankAccount("Rae Porhammer", "86753592", 37.90)
#testAccount.deposit(23.17)
#testAccount.withdraw(42)
#testAccount.withdraw(7.75)
#testAccount.get_balance()
#testAccount.add_interest(14)
#testAccount.print_statement()
Mitchell = BankAccount('Mitchell Hudson', '3141592', 0)
Mitchell.deposit(400000)
Mitchell.print_statement()
print('--------------------------')
Mitchell.add_interest(17)
Mitchell.print_statement()
print('--------------------------')
Mitchell.withdraw(150)
Mitchell.print_statement()

