from bank_manager import Bank

option = 0
bank = Bank()

while option != 7:
    print("========== Bank Management System ==========")
    print("1. Create Savings Account ")
    print("2. Create Current Account ")
    print("3. Deposit ")
    print("4. Withdraw ")
    print("5. Display One Account ")
    print("6. Display All Accounts ")
    print("7. Exit ")
    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 7.")
        continue
    if option < 1 or option > 7:
        print("Invalid Choice! Try Once Again!")
    elif option == 1:
        bank.create_savings_account()
    elif option == 2:
        bank.create_current_account()
    elif option == 3:
        if bank.deposit():
           print("Amount Deposited successfully!")
        else:
           print("Something Went Wrong. Please Try Again!")
    elif option == 4:
        if bank.withdraw():
            print("Amount Withdrawn successfully!")
        else:
            print("Something Went Wrong. Please Try Again!")
    elif option == 5:
        bank.display_one_account()
    elif option == 6:
        bank.display_all_accounts()
    else:
        break
