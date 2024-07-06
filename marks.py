# Creating a dictionary to store students' marks
marks = {
    'Student1': {'Math': 85, 'Science': 90, 'English': 78},
    'Student2': {'Math': 88, 'Science': 76, 'English': 94},
    'Student3': {'Math': 92, 'Science': 81, 'English': 87}
}

# Function to calculate total marks for each student
def calculate_total_marks(marks_dict):
    total_marks = {}
    for student, subjects in marks_dict.items():
        total_marks[student] = sum(subjects.values())
    return total_marks

# Calculating total marks
total_marks = calculate_total_marks(marks)

# Printing total marks of each student
print("Total Marks of Each Student:")
for student, total in total_marks.items():
    print(f"{student}: {total}")
