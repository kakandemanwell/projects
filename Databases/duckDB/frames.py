# import pandas as pd

# # Create students table
# students_data = {
#     'student_id': range(1, 21),
#     'student_name': [f'Student {i}' for i in range(1, 21)],
#     'class': ['Class A' if i <= 10 else 'Class B' for i in range(1, 21)]
# }
# students_df = pd.DataFrame(students_data)

# # Create marks table
# marks_data = {
#     'student_id': range(1, 21),
#     'subject1': [75, 80, 85, 90, 70, 65, 72, 78, 82, 88, 77, 83, 79, 87, 84, 89, 81, 86, 73, 76],
#     'subject2': [82, 78, 85, 88, 72, 79, 81, 83, 77, 86, 80, 75, 74, 89, 84, 87, 76, 90, 83, 79],
#     'subject3': [70, 75, 72, 80, 85, 88, 89, 84, 82, 78, 83, 79, 86, 81, 87, 90, 77, 74, 76, 73],
#     'subject4': [85, 88, 83, 80, 79, 82, 75, 78, 84, 89, 86, 81, 87, 90, 77, 74, 72, 76, 73, 81]
# }
# marks_df = pd.DataFrame(marks_data)

# # Create attendance table
# attendance_data = {
#     'student_id': range(1, 21),
#     'attendance_percent': [90, 92, 88, 95, 93, 91, 94, 89, 87, 96, 85, 92, 90, 94, 93, 91, 88, 97, 95, 86]
# }
# attendance_df = pd.DataFrame(attendance_data)

# # Display the DataFrames
# print("Students DataFrame:")
# print(students_df.head())
# print("\nMarks DataFrame:")
# print(marks_df.head())
# print("\nAttendance DataFrame:")
# print(attendance_df.head())



# -----------------------------------------------------  #

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

# Connecting to DuckDB
con = duckdb.connect(database=':memory:', read_only=False)

# Registering the dataframes as duckdb tables.
con.register('students', students_df)
con.register('marks', marks_df)
con.register('attendance', attendance_df)

# results = duckdb.sql("select * from students_df").df()

query = '''
SELECT *
FROM students
JOIN marks USING(student_id)
JOIN attendance USING(student_id)
'''

result = con.execute(query)

df = result.fetch_df()

print(df)

# print("#"* 200)

import matplotlib.pyplot as plt

# df.plot(x=df[[name]], y=df[[attendance_date]])

attendance_rate = df.groupby('name')['present'].mean() * 100
# scores = df.groupby('name')['']

# plt.figure(figsize=(10,6))
# attendance_rate.plot(kind='bar', color='skyblue')
# plt.xlabel('Student Name')
# plt.ylabel('Attendance Rate (%)')
# plt.title('Attendance Rate of Students')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()

# plt.show()

# < ---------- A scores report ---------- >

# Calculate statistics for each subject
subject_stats = df[['subject1', 'subject2', 'subject3', 'subject4']].describe()

# Transpose the dataframe for better readability
subject_stats = subject_stats.T

# Print the scores report
print("Scores Report:")
print(subject_stats)


# < ---------- A scores report ---------- >

for subject in ['subject1', 'subject2', 'subject3', 'subject4']:
    plt.hist(df[subject].mean(), bins=10, alpha=0.5, label=subject)

plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Distribution of Scores for Each Subject')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# plot of average scores per subject.

avg_scores = df[['subject1', 'subject2', 'subject3', 'subject4']].mean()

# Plot histogram with subjects on the x-axis
plt.figure(figsize=(10, 6))
plt.bar(avg_scores.index, avg_scores.values, color='skyblue')
plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.title('Average Scores for Each Subject')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot line graph with subjects on the x-axis
plt.figure(figsize=(10, 6))
plt.plot(avg_scores.index, avg_scores.values, marker='o', color='skyblue', linestyle='-')
plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.title('Average Scores for Each Subject')
plt.grid(True)
plt.tight_layout()
plt.show()