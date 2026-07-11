contacts = set()
option = 0
def add_contact():
    contact = input("Enter number: ")
    if len(contact) != 10:
        print("Invalid input try again!")
    else:
        contacts.add(contact)
        print("Contact Added Successfully!")
    
def show_contacts():
    if not contacts:
        print("No Contacts Available")
    else:
        for contact in contacts:
            print(contact)

def search_contact(contact):
    if contact in contacts:
        print("Contact Available")
    else:
        print("Contact Not Available")

def delete_contact(contact):
    if contact not in contacts:
        print("Contact Not Available!")
    else:
        contacts.remove(contact)
        print("Contact Deleted Successfully!")


while option != 5:
    print("========== Contact Book ==========")
    print("1. Add Contact ")
    print("2. Show Contacts ")
    print("3. Search Contact ")
    print("4. Delete Contact ")
    print("5. Exit ")
    option = int(input("Enter your choice: "))
    if option < 1 or option > 5:
        print("Invalid Choice! Try Once Again!")
    elif option == 1:
        add_contact()
    elif option == 2:
        show_contacts()
    elif option == 3:
        contact = input("Enter number: ")
        search_contact(contact)
    elif option == 4:
        contact = input("Enter number: ")
        delete_contact(contact)
    else:
        break