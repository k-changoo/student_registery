# student_registration.py
    """
    Registers a specified number of students by asking the user for their IDs.
    """
    
def register_students():
    n = int(input("Enter the number of students to register: "))

    registered_students = []
    for i in range(n):
        student_id = input(f"Enter student ID for student {i+1}: ")
        registered_students.append(student_id)

    print("Registered Students:")
    for student in registered_students:
        print(student)

if __name__ == "__main__":
    register_students()
