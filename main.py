print("Job Application Tracker")
print("1. Add an application")
print("2. Show all applications")
print("3. Exit")
choice = input("Choose an option: ")

if choice == "1":
    company = input("Company name: ")
    position = input("Position: ")
    status = input("Status: ")

    print("Application added")
    print("Company:", company)
    print("Position:", position)
    print("Status:", status)

elif choice == "2":
    print("Show all applications")

elif choice == "3":
    print("Goodbye")

else:
    print("That is not a valid option")