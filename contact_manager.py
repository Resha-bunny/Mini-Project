# # Import Contact class
from contact import Contact


# This class manages all contacts
class ContactManager:

    # Create contact list and load saved contacts
    def __init__(self):
        self.contacts = []
        self.load_contacts()


    # Add a new contact
    def add_contact(self, contact):

        self.contacts.append(contact)

        # Save contact permanently
        self.save_contacts()


    # Display all contacts
    def show_contacts(self):

        if len(self.contacts) == 0:
            print("No contacts found.")

        else:
            for contact in self.contacts:
                contact.display()


    # Search contact by name
    def search_contact(self, name):

        for contact in self.contacts:

            if contact.name.lower() == name.lower():
                return contact

        return None


    # Delete contact
    def delete_contact(self, name):

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                self.contacts.remove(contact)
                self.save_contacts()

                return True

        return False


    # Save contacts to file
    def save_contacts(self):

        print("Saving contacts...")

        file = open("contacts.txt", "w")

        for contact in self.contacts:

            file.write(
                contact.name + "," +
                contact.phone + "," +
                contact.email + "\n"
            )

        file.close()

        print("Contacts saved!")


    # Load contacts from file
    def load_contacts(self):

        try:

            file = open("contacts.txt", "r")

            for line in file:

                data = line.strip().split(",")

                if len(data) == 3:

                    contact = Contact(
                        data[0],
                        data[1],
                        data[2]
                    )

                    self.contacts.append(contact)

            file.close()

        except FileNotFoundError:
            pass
        