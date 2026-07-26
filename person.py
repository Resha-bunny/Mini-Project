# This class stores basic information of a person
class Person:

    # Constructor to initialize name and phone
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    # Display person details
    def display(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
