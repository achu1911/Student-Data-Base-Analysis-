# Final Project 2 - Alexa Chu 

import os 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Constant values
weight_score = 0.9
weight_grade = 0.1 

# 5.7:  Creating a list manually
# Initial list of students
initial_students = [
    {'student_id': 1, 'name': 'Amy', 'grade': 'A', 'score': 90},
    {'student_id': 2, 'name': 'Bob', 'grade': 'B', 'score': 80},
    {'student_id': 3, 'name': 'Gerald', 'grade': 'C', 'score': 70}
]
# 5.8: Appending a new student, Billy, to the list
new_student = {'student_id': 4, 'name': 'Billy', 'grade': 'A', 'score': 100}
initial_students.append(new_student)

# Printing the original list of students
print("Initial List of Students:")
print(initial_students)

# 8_2: Reading in a CSV of data into a data frame object using pandas 
# Change working directory
os.chdir(r"C:\Users\alexa\OneDrive\Final Project Coding - INST126") # Using a raw string to avoid needing to use backslashes

# Specify the path to CSV file
csv_file_path = "students.csv"

# Reading a CSV file into a data frame
students_df = pd.read_csv(csv_file_path)

# Display the Original Students' data frame
print("Initial Students Data Frame:")
print(students_df)

# 8_1: Using NumPy Array or Pandas Series for vectorized computation
# Function to clean the DataFrame (remove leading spaces, convert to numeric values)
def clean_dataframe(students_df):
    students_df.columns = students_df.columns.str.strip() # Remove any leading spaces from column names
    students_df['score'] = pd.to_numeric(students_df['score'], errors='coerce') # Convert 'score' column to numeric values, which will handle errors
    students_df['grade'] = students_df['grade'].str.strip()
    return students_df

students_df = clean_dataframe(students_df)

# Allow users to input their own student
while True:
    student_name = input("Enter student name (or type done to finish): ")
    if student_name.lower() == 'done':
        break 
    student_id = len(initial_students) + 1
    student_grade = input("Enter student grade (A-F): ")
    student_score = int(input("Enter student score (numeric value): "))
    new_student = {'student_id': student_id, 'name': student_name, 'grade': student_grade, 'score': student_score}
    initial_students.append(new_student)

# Display the final list of students ( with user input) as a data frame
final_students_df = pd.DataFrame(initial_students)
print(final_students_df) 

# Clean the Data Frame for final students
final_students_df = clean_dataframe(final_students_df)

# Function for calculating the weighted average score for each student
# Assume that the weights are 0.1 for test scores and 0.9 for grades
# 90% weight on scores, 10% weight on grades
def calculate_weighted_average(students_df):
    students_df['weighted_average'] = np.average( # This function computes the weighted average along the axis
        [students_df['score'], students_df['grade'].apply(lambda x: ord(x) - ord('A') + 1)], # Each grade is converted to a numeric value
        axis=0, # The averaging is done along the first rows
        weights=[weight_score, weight_grade] # Provides the weights for the two arrays
    )
# Calculate the weighted average for the final Data Frame 
calculate_weighted_average(final_students_df) 

# Display Data Frame with the calculated weighted average
print("\n Data Frame for Final Students with Weighted Average Score:")
print(final_students_df)

# 8_3: Using Pandas to get a subset of a Data Frame using a boolean
# Students with a weighted average score above the user's inputted numeric value will be placed on the dean's list
# Function to filter students for the Dean's list
def get_deans_list(students_df, threshold):
    deans_list_df = students_df[students_df['weighted_average'] > threshold]
    return deans_list_df # Return the filtered data frame 

# Get the user's threshold 
user_threshold = float(input("Enter the threshold for the dean's list (numeric value): " )) # Prompt the user to set the threshold

# Filter students
deans_list_df = get_deans_list(final_students_df, user_threshold) # Call the function

# Dean's list with user's inputted threshold:
print("\n Dean's List with Threshold: ")
print(deans_list_df)

# 8_4: Writing the changed data to CSV using Pandas
deans_list_df.to_csv('deans_list.csv', index=False)
deans_list_from_csv = pd.read_csv('deans_list.csv')
print("\n Dean's List from CSV: ")
print(deans_list_from_csv)
