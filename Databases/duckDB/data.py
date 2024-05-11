import pandas as pd
import numpy as np
import duckdb

# Students Table
students_data = {
    'student_id': range(1, 21),
    'name': ['Student {}'.format(i) for i in range(1, 21)],
    'age': np.random.randint(15, 20, 20),
    'gender': np.random.choice(['Male', 'Female'], 20),
    'class': np.random.choice(['A', 'B', 'C'], 20)
}
students_df = pd.DataFrame(students_data)

# Marks Table
marks_data = {
    'student_id': range(1, 21),
    'subject1': np.random.randint(50, 100, 20),
    'subject2': np.random.randint(50, 100, 20),
    'subject3': np.random.randint(50, 100, 20),
    'subject4': np.random.randint(50, 100, 20)
}
marks_df = pd.DataFrame(marks_data)

# Attendance Table
attendance_data = {
    'student_id': range(1, 21),
    'attendance_date': pd.date_range(start='2022-01-01', end='2022-01-20'),
    'present': np.random.choice([True, False], 20)
}
attendance_df = pd.DataFrame(attendance_data)

# Displaying first few rows of each dataframe
# print("Students Table:")
# print(students_df.head())
# print("\nMarks Table:")
# print(marks_df.head())
# print("\nAttendance Table:")
# print(attendance_df.head())


results = duckdb.sql("SELECT * FROM students_df JOIN marks_df USING(student_id) JOIN attendance_df USING(student_id)")

print(results.head())