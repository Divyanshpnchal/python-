def add_staff(database, name, department, salary, experience):
    '''This function will add new staff to the database'''
    database[name] = {'department': department, 'salary': salary, 'experience': experience}
    print("The staff is successfully added to the database.")


def view_staff(database):
    """View the list of staff in the database."""
    if database:
        print("List of Staff:")
        for name, info in database.items():
            print(f"Name: {name}, Department: {info['department']}, Salary: {info['salary']}, Experience: {info['experience']}")
    else:
        print("The database is empty.")

def search_staff(database, name):
    """Search for a staff member by name."""
    if name in database:
        info = database[name]
        print(f"Staff member '{name}' works in {info['department']} and has a salary of {info['salary']}.")
        print(f"Experience: {info['experience']}")
    else:
        print("The staff member you are searching is not present.")

def delete_staff(database, name):
    """Delete a staff member from the database."""
    if name in database:
        del database[name]
        print("The staff member is successfully deleted from the database.")
    else:
        print("The staff member you are searching is not present.")

def main():
    # Initialize database dictionaries
    teacher_database = {}
    guards_database = {}
    cleaners_database = {}
    library_database = {}
    sports_database = {}
    hostel_database = {}
    foodcourt_database = {}

    while True:
        print("\nEnter which data you want to access:")
        print("1. Teacher")
        print("2. Guards")
        print("3. Cleaners")
        print("4. Library Managers")
        print("5. Sports Managers")
        print("6. Hostel Managers")
        print("7. Food Court Staff")
        print("8. Exit")

        choice1 = input("Enter the number: ")

        if choice1 == '1':
            print("\nTeacher Database Menu:")
            print("1. Add Teacher")
            print("2. View Teachers")
            print("3. Search Teacher")
            print("4. Delete Teacher")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter teacher's name: ")
                department = input("Enter teacher's department: ")
                salary = input("Enter teacher's salary: ")
                experience = input("Enter teacher's experience: ")
                add_staff(teacher_database, name, department, salary, experience)

            elif choice == '2':
                view_staff(teacher_database)

            elif choice == '3':
                name = input("Enter teacher's name to search: ")
                search_staff(teacher_database, name)

            elif choice == '4':
                name = input("Enter teacher's name to delete: ")
                delete_staff(teacher_database, name)

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        elif choice1 == '2':
            print("\nGuards Database Menu:")
            print("1. Add Guard")
            print("2. View Guards")
            print("3. Search Guard")
            print("4. Delete Guard")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter guard's name: ")
                department = input("Enter guard's department: ")
                salary = input("Enter guard's salary: ")
                experience = input("Enter guard's experience: ")
                add_staff(guards_database, name, department, salary, experience)

            elif choice == '2':
                view_staff(guards_database)

            elif choice == '3':
                name = input("Enter guard's name to search: ")
                search_staff(guards_database, name)

            elif choice == '4':
                name = input("Enter guard's name to delete: ")
                delete_staff(guards_database, name)

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        elif choice1 == '3':
            print("\nCleaners Database Menu:")
            print("1. Add Cleaner")
            print("2. View Cleaners")
            print("3. Search Cleaner")
            print("4. Delete Cleaner")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter cleaner's name: ")
                department = input("Enter cleaner's department: ")
                salary = input("Enter cleaner's salary: ")
                experience = input("Enter cleaner's experience: ")
                add_staff(cleaners_database, name, department, salary, experience)

            elif choice == '2':
                view_staff(cleaners_database)

            elif choice == '3':
                name = input("Enter cleaner's name to search: ")
                search_staff(cleaners_database, name)

            elif choice == '4':
                name = input("Enter cleaner's name to delete: ")
                delete_staff(cleaners_database, name)

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        elif choice1 == '4':
            print("\nLibrary Managers Database Menu:")
            print("1. Add Library Manager")
            print("2. View Library Managers")
            print("3. Search Library Manager")
            print("4. Delete Library Manager")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter library manager's name: ")
                department = input("Enter library manager's department: ")
                salary = input("Enter library manager's salary: ")
                experience = input("Enter library manager's experience: ")
                add_staff(library_database, name, department, salary, experience)

            elif choice == '2':
                view_staff(library_database)

            elif choice == '3':
                name = input("Enter library manager's name to search: ")
                search_staff(library_database, name)

            elif choice == '4':
                name = input("Enter library manager's name to delete: ")
                delete_staff(library_database, name)

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")        

        elif choice1 == '5':
            print("\nSports Managers Database Menu:")
            print("1. Add Sports Manager")
            print("2. View Sports Managers")
            print("3. Search Sports Manager")
            print("4. Delete Sports Manager")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter sports manager's name: ")
                department = input("Enter sports manager's department: ")
                salary = input("Enter sports manager's salary: ")
                experience = input("Enter sports manager's experience: ")
                add_staff(sports_database, name, department, salary, experience)

            elif choice == '2':
                view_staff(sports_database)

            elif choice == '3':
                name = input("Enter sports manager's name to search: ")
                search_staff(sports_database, name)

            elif choice == '4':
                name = input("Enter sports manager's name to delete: ")
                delete_staff(sports_database, name)

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        elif choice1 == '6':
            print("\nHostel Managers Database Menu:")
            print("1. Add Hostel Manager")
            print("2. View Hostel Managers")
            print("3. Search Hostel Manager")
            print("4. Delete Hostel Manager")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter hostel manager's name: ")
                department = input("Enter hostel manager's department: ")
                salary = input("Enter hostel manager's salary: ")
                experience = input("Enter hostel manager's experience: ")
                add_staff(hostel_database, name, department, salary, experience)

            elif choice == '2':
                view_staff(hostel_database)

            elif choice == '3':
                name = input("Enter hostel manager's name to search: ")
                search_staff(hostel_database, name)

            elif choice == '4':
                name = input("Enter hostel manager's name to delete: ")
                delete_staff(hostel_database, name)

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        elif choice1 == '7':
            print("\nFood Court Staff Database Menu:")
            print("1. Add Food Court Staff")
            print("2. View Food Court Staff")
            print("3. Search Food Court Staff")
            print("4. Delete Food Court Staff")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter new staff member name: ")
                department = input("Enter department: ")
                salary = input("Enter the salary: ")
                experience = input("Enter experience: ")
                add_staff(foodcourt_database, name, department, salary, experience)

            elif choice == '2':
                view_staff(foodcourt_database)

            elif choice == '3':
                name = input("Enter staff member's name to search: ")
                search_staff(foodcourt_database, name)

            elif choice == '4':
                name = input("Enter staff member's name to delete: ")
                delete_staff(foodcourt_database, name)

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


        elif choice1 == '8':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
