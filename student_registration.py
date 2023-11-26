# student_registration.py

def register_students():
    n = int(input("Enter the number of students to register: "))

    student_list = []
    for i in range(n):
        student_id = input(f"Enter student ID for student {i+1}: ")
        student_list.append(student_id)

    print("Registered Students:")
    for student in student_list:
        print(student)

if __name__ == "__main__":
    register_students()
