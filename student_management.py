students = []

while True:

    print("\n1. Add Student")
    print("2. View Student")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter the name: ")
        students.append(name)

    elif choice == 2:
        print("Students List:")

        for student in students:
            print(student)

    elif choice == 3:
        print("Exit")
        break

    else:
        print("Not Valid")
