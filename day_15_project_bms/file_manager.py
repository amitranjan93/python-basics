from account_manager import SavingsAccount,CurrentAccount
import os

def save_accounts(accounts):
    with open("day_15_project_bms/accounts.txt", "w") as file:
        for account in accounts:
            if isinstance(account,SavingsAccount):
                file.write(f"S|{account.account_no}|{account.customer_name}|{account.balance}|{account.interest_rate}\n")
            else:
                file.write(f"C|{account.account_no}|{account.customer_name}|{account.balance}|{account.overdraft_limit}\n")

def load_accounts():
    accounts = []
    if os.path.exists("day_15_project_bms/accounts.txt"):
        with open("day_15_project_bms/accounts.txt",'r') as file:
            for line in file:
                data = line.strip().split('|')
                if data[0]=='S':
                    accounts.append(SavingsAccount(int(data[1]),data[2],float(data[3]),float(data[4])))
                else:
                    accounts.append(CurrentAccount(int(data[1]),data[2],float(data[3]),float(data[4])))
    else:
        file = open("day_15_project_bms/accounts.txt",'w')
        file.close()
    return accounts

