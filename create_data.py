import pandas as pd

data = {
    'Student Name': ['Rahul','Priya','Amit','Sneha','Rohan','Pooja','Vijay','Neha','Arjun','Kavya'],
    'Roll No': [1,2,3,4,5,6,7,8,9,10],
    'Python': [85,92,45,78,55,88,72,91,60,76],
    'Mathematics': [78,88,40,82,65,79,68,85,55,80],
    'Electronics': [90,75,50,70,60,85,74,88,65,72],
    'Attendance': [92,95,60,88,70,91,85,93,72,87]
}

df = pd.DataFrame(data)
df.to_excel('student_data.xlsx', index=False)
print('Excel file created successfully!')
