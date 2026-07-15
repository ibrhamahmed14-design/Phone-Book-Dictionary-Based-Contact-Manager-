BOOK = {
    "John Doe": "123-456-7890",
    "Jane Smith": "987-654-3210",
    "Bob Johnson": "555-555-5555",
    "Alice Brown": "111-222-3333",
    "Charlie Davis": "444-555-6666",
    "Eve Wilson": "777-888-9999",
    "Frank Miller": "000-111-2222",
    "Grace Lee": "333-444-5555",
    "Hannah Clark": "666-777-8888",
}
BOOK = {name.lower(): phone for name, phone in BOOK.items()}
def format_phone(phone):
    return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
def get_phone_number(name):
    name = name.strip().lower()
    return BOOK.get(name, "Phone number not found.")
def add_contact(name, phone_number):
    name = name.strip().lower()
    if name in BOOK.keys():
        return "Contact already exists."
    if phone_number.isdigit() and len(phone_number) == 10:
        BOOK[name] = format_phone(phone_number)
        return f"Contact {name} added with phone number {phone_number}."
    else:
        return "Invalid phone number. Please enter a 10-digit number."
def remove_contact(name):
    name = name.strip().lower()
    if name in BOOK.keys():
        del BOOK[name]
        return f"Contact {name} removed."
    else:
        return "Contact not found."
def update_contact(name, phone_number):
    name = name.strip().lower()
    if name in BOOK.keys() and phone_number.isdigit() and len(phone_number) == 10:
        BOOK[name] = format_phone(phone_number)
        return f"Contact {name} updated with new phone number {phone_number}."
    else:
        return "Contact not found or invalid phone number. Please enter a 10-digit number."
def show_contacts():
    if not BOOK:
        print("No contacts found.")
    for name, phone_number in sorted(BOOK.items()):
        print(f"{name}: {phone_number}") 
    
while True: 
    choice = input("Enter your choice (get, add, remove, update, show, exit): ").strip().lower()
    if choice == "get":
        name = input("Enter the name of the contact: ")
        print(get_phone_number(name))
    elif choice == "add":
        name = input("Enter the name of the contact: ")
        phone_number = input("Enter the phone number: ")
        print(add_contact(name, phone_number))
    elif choice == "remove":
        name = input("Enter the name of the contact: ")
        print(remove_contact(name))
    elif choice == "update":
        name = input("Enter the name of the contact: ")
        phone_number = input("Enter the new phone number: ")
        print(update_contact(name, phone_number))
    elif choice == "show":
        show_contacts()
    elif choice == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")