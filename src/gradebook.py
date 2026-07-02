gradebook = {"Alan": 89, "Sarah": 69, "Kevin": 87, "Jimmy": 68}

def add_student (name, marks):
    if name not in gradebook:
        if marks in range (1,101):
            gradebook [name] = marks
        else:
            print("Marks should be in between 1-100.")
    else:
        print("Student data already added.")

def remove_student (name):
    if name in gradebook:
        del gradebook[name]
    else:
        print("Student data not found.")


def edit_student (name, marks):
    if name in gradebook:
        if marks in range(1,101):
            gradebook[name] = marks
        else:
            print("Marks should be in between 1-100.")
    else:
        print("Student data not found.")




while True:
    print ("1. Add Student, 2. Remove Student Data, 3. Edit Student Data, 4. View All Student Data, 5. Exit")
    choice = input ("Enter Option: ")
    if choice.isdecimal():
        choice = int (choice)
        if choice == 1:
            add_student (input("Enter student name: "), int(input("Enter marks: ")))
        elif choice == 2:
            remove_student (input("Enter student name: "))
        elif choice == 3:
            edit_student (input("Enter Student Name: "),  int(input("Enter marks: ")))
        elif choice == 4:
            print(gradebook)
        elif choice == 5:
            break
        else:
            print ("Wrong Input, Try Again.")
    else:
        print ("Enter a digit.")