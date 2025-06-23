import csv

contacts = []

def load_contacts():
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
        print("Contacts loaded successfully.")
    except FileNotFoundError:
        print("No saved contacts found.")



def save_contacts():
    with open("contacts.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email", "Address"])
        writer.writeheader()
        writer.writerows(contacts)


def add_contact():
    phone_number = input("Insert your phone number: ")
    if not phone_number.isdigit():
        print("'", phone_number, "'", "isn't a digit!")
        return "Error: number isn't a digit"
    
    for c in contacts:
        if c["Phone"] == phone_number:
            print("Phone number already exists! ")
            return "Error: Phone number already exists"

    Name = input("Insert your name: ")
    Email = input("Insert your Email: ")
    address = input("Insert your adress: ")

    print("This is your information:", Name, ",", Email, ",", phone_number, ",", address, ".")

    contact = {
        "Name": Name,
        "Phone": phone_number,
        "Email": Email,
        "Address": address
    }

    contacts.append(contact)
    save_contacts()

    return "Contact added successfully!"





def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("=====CONTACTS=====")
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. Name: {c['Name']}")
            print(f"   Phone: {c['Phone']}")
            print(f"   Email: {c['Email']}")
            print(f"   Address: {c['Address']}\n")




def delete_contact():
    answer = input("Enter the phone number of the contact you want to delete: ")
    
    for c in contacts: 
        if c["Phone"] == answer:
            confirm = input('Are you sure? (y/n): ')
            if confirm == 'y': 
                contacts.remove(c)
                print(answer, "removed.")
                save_contacts()
            else:
                print("Cancelled.")
            return 

    print("Error,", answer, "doesn't exist in list.")



def show_menu():
    print("""
=========== MENU ===========
1. Add Contact
2. View Contacts
3. Search Contact
4. Remove Contact
5. Exit
============================
""")
    

def search():
    search_term = input('Enter what you want to search (email, name or address): ')
    found = False

    for c in contacts:
        if (search_term in c['Name'] or 
            search_term in c['Address'] or 
            search_term in c['Email']): 
            print("Found contact!")
            print("Name:", c['Name'])
            print("Address:", c['Address'])
            print("Email:", c["Email"])
            print("Phone:", c["Phone"])
            found = True

    if not found:
        print("No matching contact.")




def user_action():
    while True:
        show_menu()
        menu_answer = input("what do you want to do (1,2,3,4,5): ")
        if not menu_answer.isdigit():
            print("Error! write a number")
            continue
        if menu_answer == "1":
            add_contact()
        elif menu_answer == "2":
            view_contacts()
        elif menu_answer == "3":
            search()
        elif menu_answer == "4":
            delete_contact()
        elif menu_answer == "5":
            print("Bye!")
            save_contacts()

            break
        else: 
            print("invalid choice")

load_contacts()
user_action()



