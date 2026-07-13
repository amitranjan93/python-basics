
import os
def save_expenses(expenses):
    expense = open("expenses.txt",'w')
    for curr_expense in expenses:
        expense.write(f"{curr_expense['category']} | {curr_expense['amount']} | {curr_expense['date']}\n")
    expense.close()

def load_expenses(expenses):
    if os.path.exists("expenses.txt"):
        file = open("expenses.txt",'r')
        for line in file:
            parts = line.split('|')
            expenses.append({
                "category":parts[0].strip(),
                "amount": float(parts[1].strip()),
                "date":parts[2].strip()
            })
        file.close()
    else:
        file = open("expenses.txt",'w')
        file.close()
