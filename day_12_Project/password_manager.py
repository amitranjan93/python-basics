import file_manager as fm
passwords = []

class Password:
    def __init__(self,website,username,password):
        self.website = website
        self.username = username
        self.password = password

    def show(self):
        print(f"Website: {self.website}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

    def check_strength(self):
        if len(self.password) >= 8:
            return "strong"
        else:
            return "weak"
        
    def update_password(self, new_password):
        self.password = new_password
        
def add_password():
    website = input("Website: ").lower()
    username = input("Username: ")
    password = input("Password: ")
    passwords.append(Password(website,username,password))
    fm.save_passwords(passwords)
    print("Password Added Successfully!")
    
def show_passwords():
    if not passwords:
        print("No Passwords Available!")
    else:
        for password in passwords:
            password.show()
            print("-------------------------------------")

def check_password_strength():
    curr_password = input("Enter website: ").lower()
    flag = False
    for password in passwords:
        if curr_password == password.website:
            flag = True
            print(f"Password Strength: {password.check_strength()}")
    if not flag:
        print("No Website Found, Please Try Again!")

def edit_password():
    flag = False
    website = input("Enter website: ").lower()
    for password in passwords:
        if password.website == website:
            flag = True
            new_password = input("Enter new Password: ")
            password.update_password(new_password)
            print("Password Updated Successfully!")
            fm.save_passwords(passwords)
            break
    if not flag:
        print("No Website found, Please Try Again!")

def delete_password():
    website = input("Enter Website: ").lower()
    flag = False
    for password in passwords:
        if password.website == website:
            flag = True
            passwords.remove(password)
            print("Password Deleted successfully!")
            fm.save_passwords(passwords)
            break
    if not flag:
        print("Website Unavailable!")