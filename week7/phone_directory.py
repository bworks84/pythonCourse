# add contact
# update contact
# delete contact

# ** Main Program **
# while not exiting ....
# show menu
#   1 - Show contact list
#   2 - Add to contact list
#   3 - Update contact phone number
#   4 - Delete contact
#   accept command input
#   decode command and call appropriate function

print()
print("PHONE DIRECTORY PROGRAM")
print()

contact_list = {}


def list_contacts(contact_list):
    print("\n")
    print("Contacts List")
    print("-------------")
    if contact_list == {}:
        print("There are no contacts in your list")
        print("\n")
    else:
        for key in contact_list.keys():
            print(key, ":", contact_list[key])
        print()


def add_contact(contact_list):
    print("\n")
    print("Add a contact")
    print("--------------")
    name = input("Name: \n")
    phone_number = input("Phone Number: \n")
    contact_list[name] = phone_number
    print("\n")


menu_command = -1


while menu_command != 0:
    print("Commands menu")
    print("-------------")
    print("1 - Show contact list")
    print("2 - Add to contact list")
    print("3 - Update contact phone number")
    print("4 - Delete contact")
    print("0 - Exit")
    print("\n")
    menu_command = int(input("Please enter a number 0 - 4:\n"))

    if menu_command == 1:
        list_contacts(contact_list)
    elif menu_command == 2:
        add_contact(contact_list)
    elif menu_command == 3:
        print("Update a contact")
        break
    elif menu_command == 4:
        print("Delete a contact")
        break
    elif menu_command == 0:
        print("Exit menu")
        exit()
    else:
        print("Please enter a number between 0 - 4")

print("That's all folks")
print("\n")


# NOTES
# 1. Adding contact works, but not updating contact list for multiple entries
