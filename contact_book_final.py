import csv

# Step 1 Function to write and save contacts to the CSV file
def get_write_contacts(contacts):
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Address', 'Phone', 'Email'])
        writer.writerows(contacts)
    print("Contact book updated Bro!")

# step 2 Function 1 to read contacts from the CSV file so user can see whats going on.
def get_read_contacts():
    contacts = []
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
       # next(reader)  # I removed the header row code  because theres no header row Skip the header row because it does not have what we want so we go to row 2.
        for row in reader:
            contacts.append(row)
    return contacts

# Function 2 to add a new contact to the list using the sweet append function  yay ! 
def get_add_contact():
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    do_add_contact(name, address, phone, email)

def do_add_contact(name, address, phone, email):
    contacts = get_read_contacts()
    contacts.append([name, address, phone, email])
    get_write_contacts(contacts)
    print("Contact added successfully!")

# Function 3 to edit the contacts we have on our little list.
def get_edit_contact():
    contact_id = input("Enter the index of the contact you want to edit: ")

    contacts = get_read_contacts()

    if int(contact_id) < len(contacts):
        print("Contact found. Enter the new details:")

        name = input("Enter the name: ")
        address = input("Enter the address: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")

        contacts[int(contact_id)] = [name, address, phone, email]
        get_write_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print(" Sorry Contact not found!")

# Function 4 to delete the contact that we kind of dont want anymore. 
def get_delete_contact():
    contact_id = input("Enter the index or ID of the contact you want to delete: ")
    do_delete_contact(contact_id)

def do_delete_contact(contact_id):
    contacts = get_read_contacts()

    if int(contact_id) < len(contacts):
        del contacts[int(contact_id)]
        get_write_contacts(contacts)
        print("Congratulations Contact deleted successfully!")
    else:
        print(" Sorry Contact not found!")

# Function to see  all contacts that we have.
def get_view_contacts():
    contacts = get_read_contacts()

    if contacts:
        print("Contacts:")
        for i, contact in enumerate(contacts):
            print("Index:", i)
            print("Name:", contact[0])
            print("Address:", contact[1])
            print("Phone:", contact[2])
            print("Email:", contact[3])
            print()
    else:
        print("No contacts found!")

# Main program function
def main():
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. View Contacts")
        print("5. Quit")

        choice = input(" Please Enter your choice (1-5): ")

        if choice == '1':
            get_add_contact()
        elif choice == '2':
            get_edit_contact()
        elif choice == '3':
            get_delete_contact()
        elif choice == '4':
            get_view_contacts()
        elif choice == '5':
            break
        else:
            print(" Sorry Invalid choice My Guy !")



if __name__ == '__main__':
    main()