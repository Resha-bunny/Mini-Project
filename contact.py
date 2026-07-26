# # Import Person class
from person import Person


# Contact class inherits Person class
class Contact(Person):

    # Constructor to initialize contact details
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        self.email = email

    # Display complete contact information
    def display(self):
        print("----------------------")
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)