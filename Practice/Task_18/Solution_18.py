contacts = {}

def add_contact():
    while True:
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contacts[name] = number   # dictionary[key] = value
        print("Contact added successfully!")
        choice = input("Do you want to add another contact? (yes/no): ")
        if choice.lower() != "yes":
            break
     
def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Phone number: ", contacts[name])
    else:
        print("Contact not found!")
        
def delete_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        del contacts[name]
    
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
        
def show_contacts():
    if not contacts:
        print("Contact book is empty")
    else:
        print("\nAll Contacts:")
        
        for name in sorted(contacts): #Sorts contact names alphabetically
            print(name, ":", contacts[name])
            
while True:
    #This creates an infinite loop.
    #Why do we need it?
    #Because we want the contact book to keep running so the user can perform multiple operations without restarting the program.
    print("\n----- Contact Book -----")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contact")
    print("5. Exit")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        add_contact()
        
    elif choice == "2":
        search_contact()
        
    elif choice == "3":
        delete_contact()
    
    elif choice == "4":
        show_contacts()
    
    elif choice == "5":
        print("Exiting Contact Book!")
        break
    
    else:
        print("Invalid choice")