# Final Project 2 - Alexa Chu 

import os 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Student Data Base

# 5.7:  Creating a list manually
students_list = [
    {'student_id': 1, 'name': 'Amy', 'grade': 'A', 'score': 90},
    {'student_id': 2, 'name': 'Bob', 'grade': 'B', 'score': 80},
    {'student_id': 3, 'name': 'Gerald', 'grade': 'C', 'score': 70}
]

# 5.8: Appending a new student, Billy, to the list
new_student = {'student_id': 4, 'name': 'Billy', 'grade': 'A', 'score': 100}
students_list.append(new_student)

# Printing the updated list of students
print("Updated List of Students:")
print(students_list)

# 8_2: Reading in a CSV of data into a data frame object using pandas 
# Change working directory
os.chdir(r"C:\Users\alexa\OneDrive\Final Project Coding - INST126") # Using a raw string to avoid needing to use backslashes

# Specify the path to CSV file
csv_file_path = "students.csv"

# Reading a CSV file into a data frame
students_df = pd.read_csv(csv_file_path)

# Display the Original Students data frame
print("Oriignal Students Data Frame:")
print(students_df)

# 8_1: Using NumPy Array or Pandas Series for vectorized computation
# Remove any leading spaces from column names
students_df.columns = students_df.columns.str.strip()
print(students_df.columns)

# Convert 'score' column to numeric values, which will handle errors
students_df['score'] = pd.to_numeric(students_df['score'], errors='coerce')

# 
students_df['grade'] = students_df['grade'].str.strip()

# Calculating  the weighted average score for each student
# Assume that the weights are 0.1 for test scores and 0.9 for grades
# 90% weight on scores, 10% weight on grades
students_df['weighted_average'] = np.average( # This function computes the weighted average along the axis
    [students_df['score'], students_df['grade'].apply(lambda x: ord(x) - ord('A') + 1)], # Each grade is converted to a numeric value
    axis=0, # The averaging is done along the first rows
    weights=[0.9,0.1] # Provides the weights for the two arrays
    )

# Data Frame with the calculated weighted average
print("\n Data Frame with Weighted Average Score:")
print(students_df)

# 8_3: Using Pandas to get a subset of a Data Frame using a boolean
# Students with a weighted average score above a 90 will be placed on the dean's list
user_threshold = float(input("Enter the threshold for the dean's list (numeric value): " )) # Prompt the user to set the threshold
deans_list_df = students_df[students_df['weighted_average'] > user_threshold]
print(deans_list_df)

# 8_4: Writing the changed data to CSV using Pandas
deans_list_df.to_csv('deans_list.csv', index=False)
deans_list_from_csv = pd.read_csv('deans_list.csv')
print(deans_list_from_csv)

