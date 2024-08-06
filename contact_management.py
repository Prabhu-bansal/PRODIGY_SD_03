import json

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Cool! Contact {name} added.")

def view_contacts():
    if contacts:
        print("Here are your contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts yet. Add some!")

def edit_contact():
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} updated!")
    else:
        print(f"Can't find {name}. Maybe add it first?")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"{name} doesn't exist in your contacts.")

def save_contacts(filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file)
    print("Contacts saved!")

def load_contacts(filename='contacts.json'):
    global contacts
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
        print("Contacts loaded!")
    except FileNotFoundError:
        print("No saved contacts found. Let's start fresh.")

def main():
    load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Exit")
        
        choice = input("What do you want to do? (Choose a number): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            save_contacts()
        elif choice == '6':
            save_contacts()
            print("See ya! Exiting...")
            break
        else:
            print("Invalid choice. Pick a number between 1 and 6.")

if __name__ == "__main__":
    main()
