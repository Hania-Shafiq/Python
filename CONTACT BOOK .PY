NAMES = []
PHONE_NUMBERS = []

def display():
    if not NAMES: #if NAMES list is empty
        print("No contacts found.")
    else:
        for i in range(len(NAMES)):
            print(f"Name: {NAMES[i]}\t\t\t\t\tPhone Number: {PHONE_NUMBERS[i]}")

def search():
    try:
        if not NAMES:
            print("No contacts found.")
            return

        a = input("Enter name to search: ").upper()
        index = NAMES.index(a)
        print(f"Name: {NAMES[index]}\t\t\t\t\tPhone Number: {PHONE_NUMBERS[index]}")
    except ValueError:
        print("Contact not found")

def add():
    try:
        name = input("Enter Name: ").upper()
        phone_number = input("Enter Phone Number: ")
        # Check if the phone_number is numeric
        if not phone_number.isdigit():
            raise ValueError("Invalid phone number. Please enter a numeric value.")
        NAMES.append(name)
        PHONE_NUMBERS.append(phone_number)
        print("Phone Number added successfully")
    except ValueError:
        print("Error: Invalid input. Please check your input and try again.")

def delete():
    try:
        if not NAMES:
            print("No contacts found.")
            return

        a = input("Enter name to delete: ").upper()
        index = NAMES.index(a)
        NAMES.pop(index)
        PHONE_NUMBERS.pop(index)
        print("Contact deleted successfully")
    except ValueError:
        print("Contact not found")
# Load contacts from the file at the start
try:
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            data = line.split(',')
            name = data[0]
            phone_number = data[1]

            NAMES.append(name)
            PHONE_NUMBERS.append(phone_number)
except FileNotFoundError:
    print("No existing contacts found.\nStarting with an empty list.")
          
while True:
    print("""
    CONTACT BOOK OPENED
    ENTER OPERATION'S NUMBER YOU WANT TO PERFORM:
    1. DISPLAY ALL CONTACTS
    2. SEARCH A CONTACT
    3. DELETE A CONTACT
    4. ADD A CONTACT
    5. EXIT CONTACT BOOK
    """)

    choice = input("Enter your choice(number): ").strip()

    if choice == '1':
        display()
    elif choice == '2':
        search()
    elif choice == '3':
        delete()
    elif choice == '4':
        add()
    elif choice == '5':
        print("Closing the Contact Book")
        with open("contacts.txt", "w") as file:
            for name, phone_number in zip(NAMES, PHONE_NUMBERS):
                file.write(f"{name},{phone_number}\n")
        print("Contacts successfully saved.")
        print("Contact Book Closed")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")



