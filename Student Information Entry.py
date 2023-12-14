print("WELCOME TO STUDINFO BY JES RIN")
input()

students = {} # Dictionary to store student information

# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter student roll number: ")
    email = input("Enter student email: ")
    contact_number = input("Enter student contact number: ")
    students[roll_number] = {
        "name": name,
        "email": email,
        "contact_number": contact_number
    }
    print("Student added successfully!")

# Function to display all students
def display_students():
    if len(students) == 0:
        print("No students added yet!")
    else:
        print("Roll Number\tName\t\tEmail\t\tContact Number")
        for roll_number, student in students.items():
            print(f"{roll_number}\t\t{student['name']}\t\t{student['email']}\t\t{student['contact_number']}")
            # Add a blank line between each student's details for better readability. 
            # Function to search for a specific student by roll number

# Function to search for a specific student by roll number
def search_student():
     roll_number = input("Enter student roll number: ")
     
     if roll_number in students:
        student = students[roll_number]
        print(f"Name: {student['name']}")
        print(f"Email: {student['email']}")
        print(f"Contact Number: {student['contact_number']}")
     else:
        print("Student not found!") 
        # Function to update a specific student's details by roll number and field (name, email, or contact number)

# Function to update a specific student's details by roll number and field (name, email, or contact number)
def update_student():
    roll_number = input("Enter student roll number: ")
    if roll_number in students:
        field = input("Enter field to update (name, email, or contact number): ")
        if field in students[roll_number]:
            new_value = input(f"Enter new {field}: ")
            students[roll_number][field] = new_value
            print("Student's details updated successfully!")
        else:
            print("Invalid field! Please enter a valid field.")
    else:
        print("Student not found!")

# Function to delete a specific student by roll number
def delete_student():
    roll_number = input("Enter student roll number: ")
    if roll_number in students:
        del students[roll_number] # Remove the specified student's details from the dictionary.
        print("Student deleted successfully!")
    else:
        print("Student not found!")

# Main function to provide menu options and call the respective functions based on user input.
def main():
    while True:
        print("\nMenu Options:")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Search for a specific student")
        print("4. Update a specific student's details")
        print("5. Delete a specific student")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            break
        else:
            print("Invalid choice! Please enter a valid choice.")

if __name__ == "__main__":
    main()
