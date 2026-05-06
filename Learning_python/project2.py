#Contact Book CLI

def add_contact(name,phone):
    if not name.strip():
        print("Name cannot be empty")
        return
    if not phone.isdigit():
        print("Phone must contain digits only")
        return
    
    with open("contacts.txt", "a") as f:
        f.write(f"{name} | {phone}\n")

def view_contacts():
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("File not found")

def search_contact(name):
    try:
        with open("contacts.txt", "r") as f:
            found = False
            for line in f:
                if name.lower() in line.lower():
                    print(line.strip())
                    found = True

            if not found:
                print(f"Not found contacts with name: {name}")
    except FileNotFoundError:
        print("File not found")

def delete_contact(name):
    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()
        found = False
        new_lines = []
        for line in lines:
            if name in line:
                found = True
            else:
                new_lines.append(line)

        with open("contacts.txt", "w") as f:
            f.writelines(new_lines)
        if found:
            print("Contact deleted")
        else:
            print("Contact not found")

    except:
        print("No contacts yet")


while (True):
    a = input("Enter any number from 1 to 5:")

    if a == "1":
        name = input("Enter the name you want to add:")
        phone = (input("Enter the number you want to add:"))
        add_contact(name,phone)
    elif a == "2":
        view_contacts()
    elif a == "3":
        name = input("Enter the name you want to search:")
        search_contact(name)
    elif a == "4":
        name = input("Enter the name you want to delete:")
        delete_contact(name)
    elif a == "5":
        print("Exit")
        break
    else:
        print("Invalid input.Enter from 1 to 5 only")





