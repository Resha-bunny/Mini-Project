# Import required classes
from contact import Contact
from contact_manager import ContactManager


# Create ContactManager object
manager = ContactManager()


# Main program loop
while True:


    # Display menu
    print("\n===== Contact Directory =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


    # Take user choice
    choice = input("Enter your choice: ")



    # Add contact
    if choice == "1":

        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")


        # Create contact object
        contact = Contact(name, phone, email)


        # Save contact
        manager.add_contact(contact)

        print("Contact added successfully!")



    # View contacts
    elif choice == "2":

        print("\nContact List:")

        manager.show_contacts()



    # Search contact
    elif choice == "3":

        name = input("Enter name to search: ")


        result = manager.search_contact(name)


        if result:

            print("\nContact Found:")
            result.display()

        else:

            print("Contact not found.")



    # Delete contact
    elif choice == "4":

        name = input("Enter name to delete: ")


        result = manager.delete_contact(name)


        if result:

            print("Contact deleted successfully!")

        else:

            print("Contact not found.")



    # Exit program
    elif choice == "5":

        print("Thank you for using Contact Directory!")
        break



    else:

        print("Invalid choice!")