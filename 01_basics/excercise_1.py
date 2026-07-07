"""
Task:
Create a program that stores several students and their marks.
Requirements:
Store student names and marks in a dictionary.
Print whether each student passed or failed (pass mark = 50).
Calculate the average mark.
"""

result_book = {"Ali": 48, "Abdullah": 97, "Shaeer": 77}

for name, marks in result_book.items():
    if marks > 50:
        print(f"{name} -> Passed")
    else:
        print(f"{name} -> Failed")

# Calculate average
sum = 0
total_students = 0
for _, marks in result_book.items():
    sum += marks
    total_students += 1

average = sum / total_students

print(f"Average: {average}")
