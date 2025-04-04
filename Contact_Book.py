import os
from colorama import init, Fore, Back, Style

init(autoreset=True)  # Initialize colorama

def print_border(width=90):
    print(Fore.CYAN + "=" * width)

class Contact:
    def __init__ (self):
        self.name = ""
        self.phone_number = 0
        self.email = ""
        self.address = ""

def add_contact():
    print_border()
    print(Fore.GREEN + "ADD NEW CONTACT".center(90))
    print_border()
    if os.path.exists("ContactNumber.txt"):
        f1 = open("ContactNumber.txt","r")
        nm = int(f1.read())
        f1.close()
    else:
        nm = 0

    n = int(input("Enter the number of contact: "))
    cb = []
    for i in range(n):
        print(f"\nEnter the detail of {i+1+nm} Contact.")
        c = Contact()
        c.name = input("Enter name:")
        c.phone_number = input("Enter Phone number: ")
        c.email = input("Enter Email: ")
        c.address = input("Enter Address: ")
        cb.append(c)

    f = open("Contact_detail.txt","a")
    # f.write(f"We have total number of contact: {n}\n\n")
    for i in range(n):
        f.write(f"Contact Number: {i+1+nm}\nName: {cb[i].name}\nPhone Number: {cb[i].phone_number}\nEmail: {cb[i].email}\nAddress: {cb[i].address}\n\n")
    f.close()
    f1 = open("ContactNumber.txt","w")
    f1.write(f"{n+nm}")
    f1.close()
    print(Fore.GREEN + "Contact added successfully")

def view_contact():
    print_border()
    print(Fore.YELLOW + "CONTACT LIST".center(90))
    print_border()
    if os.path.exists("Contact_detail.txt"):
        with open("Contact_detail.txt", "r") as f:
            content = f.read()
            print(Fore.WHITE + content if content else "No contacts available.")
    else:
        print(Fore.RED + "No contacts available.")

def search_contact():
    print_border()
    print(Fore.YELLOW + "SEARCH CONTACT".center(90))
    print_border()
    search = input("Enter the name or phone number to search: ").strip().lower()
    if not search:
        print("Search term cannot be empty.")
        return
    
    if os.path.exists("Contact_detail.txt"):
        with open("Contact_detail.txt", "r") as f:
            lines = f.readlines()
    else:
        print("No contacts available to search.")
        return
    
    found = False
    current_contact = []
    
    for line in lines:
        if line.strip() == "":
            continue
        current_contact.append(line.strip())
        # If the line starts a new contact and current_contact is not empty, it means we have reached the end of a contact
        if line.strip().startswith("Contact Number") and current_contact and len(current_contact) > 1:
            # Check if the search term is in any of the current contact entries
            if any(search in entry.lower() for entry in current_contact[:-1]):
                found = True
                print("\n".join(current_contact[:-1]), "\n")
            current_contact = [line.strip()]
    
    # After the loop, check the last collected contact
    if current_contact and any(search in entry.lower() for entry in current_contact):
        found = True
        print("\n".join(current_contact), "\n")
    
    if not found:
        print("Contact not found.")

def update_contact():
    print_border()
    print(Fore.YELLOW + "UPDATE CONTACT".center(90))
    print_border()
    search = input("Enter the name or phone number of the contact to update: ").strip().lower()
    if not search:
        print("Search term cannot be empty.")
        return
    
    if not os.path.exists("Contact_detail.txt"):
        print("No contacts available to update.")
        return

    with open("Contact_detail.txt", "r") as f:
        lines = f.readlines()

    found = False
    updated_lines = []
    current_contact = []

    for line in lines:
        if line.strip() == "":
            if current_contact:
                if any(search in entry.lower() for entry in current_contact):
                    found = True
                    print("Current contact details:")
                    print("\n".join(current_contact))
                    print("\nEnter new details:")
                    name = input("Enter name: ")
                    phone_number = input("Enter phone number: ")
                    email = input("Enter email: ")
                    address = input("Enter address: ")
                    contact_number = current_contact[0]
                    updated_contact = [
                        contact_number, 
                        f"Name: {name}", 
                        f"Phone Number: {phone_number}", 
                        f"Email: {email}", 
                        f"Address: {address}", 
                        ""
                    ]
                    updated_lines.extend(updated_contact)
                else:
                    updated_lines.extend(current_contact + [""])
                current_contact = []
        else:
            current_contact.append(line.strip())

    # Check the last contact in case the file doesn't end with an empty line
    if current_contact:
        if any(search in entry.lower() for entry in current_contact):
            found = True
            print("Current contact details:")
            print("\n".join(current_contact))
            print("\nEnter new details:")
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_number = current_contact[0]
            updated_contact = [
                contact_number, 
                f"Name: {name}", 
                f"Phone Number: {phone_number}", 
                f"Email: {email}", 
                f"Address: {address}", 
                ""
            ]
            updated_lines.extend(updated_contact)
        else:
            updated_lines.extend(current_contact + [""])

    if found:
        with open("Contact_detail.txt", "w") as f:
            for line in updated_lines:
                f.write(line + "\n")
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    print_border()
    print(Fore.RED + "DELETE CONTACT".center(90))
    print_border()
    search = input("Enter the name or phone number of the contact to delete: ").strip().lower()
    if not search:
        print("Search term cannot be empty.")
        return
    
    if not os.path.exists("Contact_detail.txt"):
        print("No contacts available to delete.")
        return

    with open("Contact_detail.txt", "r") as f:
        lines = f.readlines()

    found = False
    updated_lines = []
    current_contact = []

    for line in lines:
        if line.strip() == "":
            if current_contact:
                if any(search in entry.lower() for entry in current_contact):
                    found = True
                    print("Deleting contact:")
                    print("\n".join(current_contact))
                else:
                    updated_lines.extend(current_contact + [""])
                current_contact = []
        else:
            current_contact.append(line.strip())

    if current_contact and any(search in entry.lower() for entry in current_contact):
        found = True
        print("Deleting contact:")
        print("\n".join(current_contact))
    else:
        updated_lines.extend(current_contact + [""])

    if found:
        with open("Contact_detail.txt", "w") as f:
            for line in updated_lines:
                f.write(line + "\n")
            f.write("This contact detail was deleted.")
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_menu():
    print_border()
    print(Fore.BLUE + "CONTACT BOOK MANAGEMENT SYSTEM".center(90))
    print_border()
    print(Fore.CYAN + """
    1. Add New Contact
    2. View Contact List
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    """)
    print_border()
    return input(Fore.YELLOW + "Enter your choice (1-5): " + Fore.WHITE)

def main():
    while True:
        choose = display_menu()
        
        if choose == "1":
            add_contact()
        elif choose == "2":
            view_contact()
        elif choose == "3":
            search_contact()
        elif choose == "4":
            update_contact()
        elif choose == "5":
            delete_contact()
        else:
            print(Fore.RED + "Invalid choice. Try again.")
        
        if input(Fore.YELLOW + "\nDo you want to continue? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    print(Fore.GREEN + "\nWelcome to Contact Book Management System!")
    main()
    print(Fore.GREEN + "\nThank you for using Contact Book Management System!")