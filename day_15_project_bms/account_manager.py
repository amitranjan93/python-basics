class Account:
    def __init__(self,account_no, customer_name, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0!")
            return False
        self.balance += amount
        return True

    def withdraw(self,amount):
        if amount <=0 :
            print("Amount must be greater than 0!")
            return False
        elif amount > self.balance:
            print("Insufficient balance!")
            return False
        else:
            self.balance -= amount
            return True

    def display(self):
        print('======== Account Details ===========')
        print(f"Account Number: {self.account_no}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Balance: {self.balance}")
        if isinstance(self,SavingsAccount):
            print("Account Type: Savings Account")
        else:
            print("Account Type: Current Account")

class SavingsAccount(Account):

    def __init__(self, account_number, customer_name, balance, interest_rate):
        super().__init__(account_number,customer_name,balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = (self.interest_rate / 100) * self.balance
        self.balance += interest
        print("Interest credited successfully.")

class CurrentAccount(Account):

    def __init__(self, account_no, customer_name, balance,overdraft_limit):
        super().__init__(account_no, customer_name, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <=0 :
            print("Amount must be greater than 0!")
            return False
        if self.balance - amount < -self.overdraft_limit:
            print("Insufficient balance!")
            return False
        self.balance -= amount
        return True




