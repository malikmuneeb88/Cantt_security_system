contact_book = []

def add_contact():
    name = input("Enter contact's name:\n")
    number = input("Enter contact number:\n")
    email = input("Enter contact's email:\n")
    address = input("Enter contact's adress:\n")
    
    contact = f"{name}, {number}, {email}, {address}\n"
    
    with open('contact.txt', 'a') as file:
        file.write(contact)
        # print(contact)
    print("Contact detalils added succefully!")
add_contact()


def view_contact():
    with open('contact.txt', 'r') as file:
        details = file.read()
    print("The details are as follows: \n")
    print(details)

view_contact()

def delete_contact():
    user = input("Enter contact u want to delete\: n")
    