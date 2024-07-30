# Get the number of students to register
num_students = int(input('Number of students getting registered: '))

# Open a text file for writing registration data of students
with open("reg_form.txt", "w") as file:
    # Write the header of te registration form
    file.write("Exam Registration Form\n\n")

# Create a loop to collect ID numbers and signature
    for i in range(1, num_students + 1):
        # Get student ID from user input
        student_id = input(f"Enter Student ID number {i}: ")
        # Write student ID and signature, next to it add space for the signature
        file.write(f"\nStudent {i} ID: {student_id}\t\tSignature of student:_________________\n\n")

# confirmation message that entry is successful
print(f"Registration data has been written to 'reg_form.txt'.")