import csv

print()
print("PHONE DIRECTORY PROGRAM")
print()

# phone_dir = {"Test": "123-457-2936"}

# read_csv --> func reads data from a CSV file. Initiates new dictionary, sets a boolean to use later,
# with open reads the file and gives alias (infile), var reader given value of infile read by csv.reader function.
# start a for loop that looks at each row in the CSV file, if the first line is true, it will set the value to false, so that every other row is executed (added as an entry). Then return the phone_dir dictionary


def read_CSV(csv_file):
    phone_dir = {}
    first_line = True
    with open(csv_file, mode="r") as infile:
        reader = csv.reader(infile, delimiter=",")
        for row in reader:
            if first_line:
                first_line = False
            else:
                phone_dir[row[0]] = row[1]
        return phone_dir

# write_csv --> takes in a csv file, a dictionary containing the data to be written to the csv file, a two vars
# representing the headers.
# 35 and 36 - With open opens the csv file in write mode gives it an alias,
# writer variable is assigned the value of the result from csv.writer function taking in the csv file, separates
# values by a comma.
# 38 - start a for loop that iterates through the keys, writes rows based off of key and key value.
# 42 - if item is not in the phone_dir already, call write_csv function and write the name and number to the csv file


def write_CSV(csv_file, phone_dir, column1, column2):
    with open(csv_file, mode="w", newline="") as out_file:
        writer = csv.writer(out_file, delimiter=",")
        writer.writerow([column1, column2])
        for item in phone_dir:
            writer.writerow([item, phone_dir[item]])
            # Modify the directory and save it
            if not item in phone_dir:
                write_CSV(phone_list_filepath,
                          phone_dir, "name", "number")
                print(phone_dir)

# list_contact --> if phone dir is empty, print a default statement, else loop through keys in phone dir
# print the key and value


def list_contacts(phone_directory):
    print("\n")
    print("Contacts List")
    print("-------------")
    if phone_directory == {}:
        print("There are no contacts in your list")
        print("\n")
    else:
        # working on sorting list alphabetically by keys
        # myTest = list(phone_directory.keys())
        # myTest.sort()
        # sorted_dict = {i: phone_directory[i] for i in myTest}
        # print(sorted_dict)
        for key in phone_directory.keys():
            print(key, ":", phone_directory[key])
        print()

# add_contact --> take in name and number from user
# call write_csv function and write new inputs to csv file


def add_contact(phone_directory):
    print("\n")
    print("Add a contact")
    print("--------------")
    name = input("Name: \n")
    phone_number = input("Phone Number: \n")
    phone_directory[name] = phone_number
    write_CSV(phone_list_filepath, phone_directory, "name", "number")
    print("\n")

# update_contact --> take in name and number to update
# check if the name is in the phone dir already, if not produce default statement
# if it is in directory, write_csv data to file with new inputs


def update_contact(phone_directory):
    print("\n")
    print("Update contact list")
    print("----------------")
    name = input("Find by Name:\n")
    number = input("Enter new phone number:\n")
    if name in phone_directory:
        phone_directory[name] = number
        write_CSV(phone_list_filepath, phone_directory, "name", "number")
        print(f"{name} was updated")
    else:
        print(f"{name} not found")

# remove_contact --> take in name to delete, check if it exists, if it does del from phone dir
# update csv file using function call to write_csv


def remove_contact(phone_directory):
    print("\n")
    print("Remove a contact")
    print("-----------------")
    name = input("Name:\n")
    if name in phone_dir:
        del phone_directory[name]
        write_CSV(phone_list_filepath, phone_directory, "name", "number")
        print(f"{name} was removed from contact list")
    else:
        print(f"{name} not found")

# make variable to store file path to csv file
# make variable to store data in csv file to be called in functions for this program


phone_list_filepath = "../week7/phone_contact.csv"
phone_dir = read_CSV(phone_list_filepath)
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

# call write_csv function after every command to save data in case of error in program

    if menu_command == 1:
        list_contacts(phone_dir)
    elif menu_command == 2:
        add_contact(phone_dir)
        write_CSV(phone_list_filepath, phone_dir, "name", "number")
    elif menu_command == 3:
        update_contact(phone_dir)
        write_CSV(phone_list_filepath, phone_dir, "name", "number")
    elif menu_command == 4:
        remove_contact(phone_dir)
        write_CSV(phone_list_filepath, phone_dir, "name", "number")
    elif menu_command == 0:
        print("Exit menu")
        exit()
    else:
        print("Please enter a number between 0 - 4")


print("That's all folks")
print("\n")
