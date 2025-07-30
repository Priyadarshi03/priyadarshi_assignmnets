''' 
Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''

student_data = {'Maya':20, 'Aman':30, 'Karan':40, 'Rahul':20}

student_name = input("Enter the student's name: ")

if student_name in student_data:
    students_marks = student_data[student_name]
    print(f"{student_name.capitalize()}'s marks: {students_marks}")
else:
    print(f"Student {student_name.capitalize()} not found.")

