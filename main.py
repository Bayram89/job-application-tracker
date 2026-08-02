applications = []

while True:
    print()
    print("Job Application Tracker")
    print("1. Add an application")
    print("2. Show all applications")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        company = input("Company name: ")
        position = input("Position: ")
        status = input("Status: ")

        application = {
            "company": company,
            "position": position,
            "status": status
        }

        applications.append(application)

        print("Application added")
        print("Number of applications:", len(applications))

    elif choice == "2":
        print("Show all applications")

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("That is not a valid option")