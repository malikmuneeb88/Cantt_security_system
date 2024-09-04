contact_book = []

def add_contact():
    name = input("Enter contact's name:\n")
    number = input("Enter contact number:\n")
    email = input("Enter contact's email:\n")
    address = input("Enter contact's adress:\n")
    
    contact = f"{name}, {number}, {email}, {address}\n"
    print("\n")
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
    with open('contact.txt', 'r') as file:
        content = file.readlines()
    user = input("Enter a contact you want to delete: \n")
    
    sum = 0
    for line in content:
        if user in line:
            content.remove(line)
            print(content)
            sum += 1

    if sum == 1:
        with open('contact.txt', 'w') as file:
            file.writelines(content)
        print(f"Contact {user} has been updated")
    else:
        print("Content not updated")

delete_contact()