class Contact:
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"
    ###########################################################################
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    
    def display_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts found")
        else:
            for contact in self.contacts:
                print(contact)
                print("-" * 20)

manager = ContactManager()
manager.add_contact(Contact("Aya", "123456789", "aya@example.com"))
manager.add_contact(Contact("Layan", "987654321", "layan@example.com"))
options = ["1. Add a contact", "2. Remove a contact", "3. Search a contact", "4. Display all contacts", "5. Exit"]

while True:
    print("Welcome to the Contact Manager")
    print("Please choose an option:")
    for option in options:
        print(option)
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter the name: ")
        phone = input("Enter the phone: ")
        email = input("Enter the email: ")
        contact = Contact(name, phone, email)
        manager.add_contact(contact)
        print("Contact added successfully")
    elif choice == "2":
        name = input("Enter the name of the contact to remove: ")
        result = manager.remove_contact(name)
        if result:
            print("Contact removed successfully")
        else:
            print("Contact not found")
    elif choice == "3":
        name = input("Enter the name of the contact to search: ")
        contact = manager.search_contact(name)
        if contact is None:
            print("Contact not found")
        else:
            print(contact)
    elif choice == "4":
        manager.display_contacts()
    elif choice == "5":
        print("Thank you for using the Contact Manager")
        break
    else:
        print("Invalid choice, please try again")
