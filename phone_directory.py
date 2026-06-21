phone_directory = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}

while True:
    choice = input("Search by (1) Number, (2) Name, (3) Add new contact, or 'exit' to quit: ")

    if choice == "exit":
        print("Goodbye!")
        break

    if choice == "1":
        number = input("Enter a phone number: ")
        if len(number) == 10 and number.isdigit():
            if number in phone_directory:
                print(phone_directory[number])
            else:
                print("Sorry, the number is not found")
        else:
            print("This is invalid number")

    elif choice == "2":
        name = input("Enter a name: ")
        found = False
        for num, person in phone_directory.items():
            if person == name:
                print(num)
                found = True
        if not found:
            print("Sorry, the name is not found")

    elif choice == "3":
        new_number = input("Enter the new phone number: ")
        if len(new_number) == 10 and new_number.isdigit():
            new_name = input("Enter the contact name: ")
            phone_directory[new_number] = new_name
            print("Contact added successfully!")
        else:
            print("This is invalid number")

    else:
        print("Please enter 1, 2, or 3")