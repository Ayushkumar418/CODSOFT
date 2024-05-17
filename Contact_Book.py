import os
class Contact:
    def __init__ (self):
        self.name = ""
        self.phone_number = 0
        self.email = ""
        self.address = ""

def add_contact():
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
    print("Contact added successfully")
    
def view_contact():
    print("Details of Contacts".center(90))
    if os.path.exists("Contact_detail.txt"):
        with open("Contact_detail.txt", "r") as f:
            print(f.read())
    else:
        print("No contacts available.")

def search_contact():
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


def main():
    print("\n")
    print("Welcome to the contact book".center(90))
    choose = input("Enter 1 to add contact.\nEnter 2 to View contact list.\nEnter 3 to Search contact\nEnter 4 to Update contact.\nEnter 5 to delete contact\nEnter: ")

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
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
