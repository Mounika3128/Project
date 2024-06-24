contacts = []

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print(f"Contact '{name}' added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
        return
    for contact in found_contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
    search_term = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print(f"Updating contact '{contact['name']}'")
            contact['name'] = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            print("Contact updated.")
            return
    print("No contact found.")

def delete_contact():
    search_term = input("Enter name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            contacts.remove(contact)
            print(f"Contact '{contact['name']}' deleted.")
            return
    print("No contact found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact management system.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
