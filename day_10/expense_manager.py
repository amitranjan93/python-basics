import file_manager

expenses = []

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    date = input("Date in DD/MM/YYYY format: ")
    if not category:
        print("Category cannot be empty!")
    elif amount < 0:
        print("Amount cannot be negative")
    else:
        expenses.append({"category": category, "amount":amount, "date":date })
        print("Expense Added Successfully!")
        file_manager.save_expenses(expenses)
        

def show_expenses():
    if not expenses:
        print("No Expenses available!")
    else:
        for expense in expenses:
            print(f"Category: {expense['category']}")
            print(f"Amount: {expense['amount']}")
            print(f"Date: {expense['date']}")
            print("--------------------------------------")

def search_expense():
    search_category = input("Enter Category: ")
    flag = False
    for expense in expenses:
        if expense["category"] == search_category:
            flag = True
            print(f"Category: {expense['category']}")
            print(f"Amount: {expense['amount']}")
            print(f"Date: {expense['date']}")
            print("--------------------------------------")
    if not flag:
        print("No Expense Found!")

def delete_expense():
    search_category = input("Enter Category: ")
    flag = False
    for expense in expenses[:]:
        if expense["category"] == search_category:
            expenses.remove(expense)
            flag = True

    if not flag:
        print("No Expense Found!")
    else:
        file_manager.save_expenses(expenses)
        print("Expense(s) deleted successfully!")

def show_total_expense():
    total = 0
    if not expenses:
        print("No Expenses Available!")
    else:
        for expense in expenses:
            total+=expense["amount"]
        print(f"Total expense: {total:.2f}")
