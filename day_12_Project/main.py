import password_manager as pm
import file_manager as fm

option = 0

fm.load_passwords(pm.passwords)
while option != 6:
    print("========== Password Vault ==========")
    print("1. Add Password ")
    print("2. Show Passwords ")
    print("3. Check Password Strength ")
    print("4. Edit Password ")
    print("5. Delete Password ")
    print("6. Exit ")
    option = int(input("Enter your choice: "))
    if option < 1 or option > 6:
        print("Invalid Choice! Try Once Again!")
    elif option == 1:
        pm.add_password()
    elif option == 2:
        pm.show_passwords()
    elif option == 3:
        pm.check_password_strength()
    elif option == 4:
        pm.edit_password()
    elif option == 5:
        pm.delete_password()
    else:
        break
