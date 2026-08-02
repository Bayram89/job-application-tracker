import json

try:
    with open("applications.json", "r") as file:
        applications = json.load(file)
except FileNotFoundError:
    applications = []

while True:
    print()
    print("Job Application Tracker")
    print("1. Add an application")
    print("2. Show all applications")
    print("3. Update application status")
    print("4. Exit")

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

        with open("applications.json", "w") as file:
            json.dump(applications, file)

        print("Application added")
        print("Number of applications:", len(applications))

    elif choice == "2":
        if len(applications) == 0:
            print("No applications found")
        else:
            application_number = 1

            for application in applications:
                print()
                print("Application number:", application_number)
                print("Company:", application["company"])
                print("Position:", application["position"])
                print("Status:", application["status"])

                application_number = application_number + 1

    elif choice == "3":
        if len(applications) == 0:
            print("No applications found")
        else:
            application_number_text = input("Application number: ")

            if application_number_text.isdigit():
                application_number = int(application_number_text)

                if application_number >= 1 and application_number <= len(applications):
                    new_status = input("New status: ")

                    applications[application_number - 1]["status"] = new_status

                    with open("applications.json", "w") as file:
                        json.dump(applications, file)

                    print("Status updated")
                else:
                    print("Application number not found")
            else:
                print("Please enter a number")

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("That is not a valid option")