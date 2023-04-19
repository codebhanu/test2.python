phoneDirectory = {}
print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
print("1.Add a record.")
print("2.Search a record.")
print("3.Change a record.")
print("4.Delete a record.")
print("5.Quit")

first_iteration = True
while True:
    if not first_iteration:
        print("Menu")
        print("1.Add a record.")
        print("2.Search a record.")
        print("3.Change a record.")
        print("4.Delete a record.")
        print("5.Quit")

    chice = int(input("Enter your choice: "))
    if chice == 1:
        name_to_be = (input("Enter name:"))

        while True:
            phone_num = (input("Enter the new 10-digit phone number: "))
            if len(phone_num) == 10 and phone_num.isdigit():

                phoneDirectory.update({name_to_be: phone_num})
                print("Record Added")
                break
            else:
                print("Invalid phone number. Please enter a 10-digit number.")

    elif chice == 2:
        searched = input("Enter the name to  search:")
        if searched in phoneDirectory:
            print(f"{searched}:{phoneDirectory[searched]}")
        else:
            print("There is no such records")
    elif chice == 3:
        updt = input("Enter name:")

        if updt in phoneDirectory:
            while True:
                new_num = (input("Enter new 10-digit phone number"))
                if len(new_num) == 10 and new_num.isdigit():
                    phoneDirectory.update({updt: new_num})
                    print("Record updated")
                    break
                else:
                    print("Invalid phone number. Please enter a 10-digit number.")
        else:
            print("items does not exist")
    elif chice == 4:
        dlt = input("Enter name:")
        if dlt in phoneDirectory:
            phoneDirectory.pop(dlt)
            print("Record deleted")

        else:
            print("Record does not exist")
    elif chice == 5:
        print("Thank you for using Phone directory")
        break

    else:
        print("Wrong option Entered")

    first_iteration = False
