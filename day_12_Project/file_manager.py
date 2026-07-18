import os
import password_manager as pm

def load_passwords(passwords):
    if not os.path.exists('day_12\Password.txt'):
        file = open('day_12\Password.txt','w')
        file.close()
        return
    else:
        file = open('day_12\Password.txt','r')
        for line in file:
            website, username, password = line.strip().split("|")
            passwords.append(pm.Password(website, username, password))
        file.close()

def save_passwords(passwords):
    file = open('day_12\Password.txt','w')
    for data in passwords:
        file.write(f"{data.website}|{data.username}|{data.password}\n")
    file.close()
