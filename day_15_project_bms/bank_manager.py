from account_manager import CurrentAccount,SavingsAccount
import file_manager as fm
class Bank:
    def __init__(self):
        self.accounts = fm.load_accounts()

    def add_account(self,account):
        self.accounts.append(account)
        fm.save_accounts(self.accounts)  

    def get_valid_integer(self,prompt,min_value, max_value):
        while True:
            try:
                number = int(input(f"Enter {prompt}: "))  
                if min_value <= number <= max_value:
                    return number
                else:
                    print(f"{prompt} must be in between {min_value} and {max_value}. Please try again.")
            except ValueError:
                print(f"{prompt} must be an integer. Please try again.")

    def get_valid_float(self,prompt, min_value, max_value):
            while True:
                try:
                    number = float(input(f"Enter {prompt}: " ))
                    if min_value <= number <= max_value:
                        return number
                    else:
                        print(f"{prompt} must be in between {min_value} and {max_value}. Please try again.")
                except ValueError:
                    print(f"{prompt} must be an valid number. Please try again.")

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return False
        for account in self.accounts:
            account.display()

    def find_account(self,account_number):
        for account in self.accounts:
            if account.account_no == account_number:
                return account
        return None

    def deposit(self):
        account_number = self.get_valid_integer("Account Number",0,9999999)
        amount = self.get_valid_float("Amount",0,999999999)
        account = self.find_account(account_number)
        if account:
            if account.deposit(amount):
                fm.save_accounts(self.accounts)
                return True
            else:
                return False
        else:
            print("Account Not Found")
            return False

    def withdraw(self):
        account_number = self.get_valid_integer("Account Number",0,9999999)
        amount = self.get_valid_float("Amount",0,999999999)
        account = self.find_account(account_number)
        if account:
            if account.withdraw(amount):
                fm.save_accounts(self.accounts)
                return True
            else:
                return False
        else:
            print("Account Not Found")
            return False


    def create_savings_account(self):
        while True:
            account_number = self.get_valid_integer("Account Number",0,9999999)
            if self.find_account(account_number):
                print("Account Number already exist. Please Try Again!")
            else:
                break
        name = input("Enter Customer Name: ")
        balance = self.get_valid_float("Balance",0,999999999)
        interest_rate = self.get_valid_float("Interest Rate",0,100)
        self.add_account(SavingsAccount(account_number,name,balance,interest_rate))  
        print("Account Successfully Created") 

    def create_current_account(self):
        while True:
            account_number = self.get_valid_integer("Account Number",0,9999999)
            if self.find_account(account_number):
                print("Account Number already exist. Please Try Again!")
            else:
                break
        name = input("Enter Customer Name: ")
        balance = self.get_valid_float("Balance",0,999999999)
        overdraft_limit = self.get_valid_float("OverDraft Limit",0,10000)
        self.add_account(CurrentAccount(account_number,name,balance,overdraft_limit))  
        print("Account Successfully Created")      

    def display_one_account(self):
        account_number = self.get_valid_integer("Account Number",0,9999999)
        account = self.find_account(account_number)
        if account:
            account.display()
            return
        print("No Account found with this Account Number!")