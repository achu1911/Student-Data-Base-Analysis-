# Final Project 2 - Alexa Chu 
""" # Final Project - Student Database Analysis
# Overview
This project involves analyzing a student data base to calculate the weighted average scores for each students and identify which students qualify for the dean's list.

## Project Structure:
- 'students.csv': CSV file containing the student database.
- 'denas_list.csv': CSV file containing the list of students on the dean's list.

## Features:  
# 1. Creating a student list manually
- Manually created a list of students with their student IDs, names, grades, and test scores.

# 2. Appending a new student
- Appended a new student, Billy, to the existing list.

# 3. Reading data from CSV
- I utilized pandas to read data from a CSV file into a DataFrame.

# 4. Data Cleaning 
- Removed any leading spaces from column names.
- Converted the 'score' column to numeric values.
- Stripped leading and trailing spaces from the 'grade' column.

# 5. Calculated weighted average
- Calculated the weighted average score for each student.

# 6. Identifying students on the Dean's List
- Allowed to user to input the threshold (numeric value).
- Identified and displayed students with a weighted average score above the threshold. 

# 7. Writing the results to CSV
- Wrote out the information of students on the dean's list to a new CSV file.

# 8. User Interaction
- Allows user to input a list of student names separated by commmas.
- Prompts the user to set a threshold for identifying students on the Dean's List.

# 9. Regular Expression
- A regular expression is employed to check if a student's name starts with 'A'. 
- Regular expressions are used to extract parts of a string.

## How to Use
1. Clone the repository.
2. Ensure you have the required dependencies installed (`pip install pandas numpy matplotlib`).
3. Run the script: `python final_project.py`

## Author
Alexa Chu

## License
This project is licensed under the [MIT License](LICENSE). 
""" 
import os 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import re

# Constant values
weight_score = 0.9
weight_grade = 0.1 

# 8_1: Using NumPy Array or Pandas Series for vectorized computation
# Function to clean the DataFrame (remove leading spaces, convert to numeric values)
def clean_dataframe(students_df):
    students_df.columns = students_df.columns.str.strip() # Remove any leading spaces from column names
    students_df['score'] = pd.to_numeric(students_df['score'], errors='coerce') # Convert 'score' column to numeric values, which will handle errors
    students_df['grade'] = students_df['grade'].str.strip()
    return students_df

# Allow users to input their own student
def get_user_input(student_id):
    student_name = input("Enter student name (or type done to finish): ") # Asks for the student's name
    if student_name.lower() == 'done': 
        return None 
    student_grade = input("Enter student grade (A-F): ").upper() # input the student's grade
    try:
        student_score = int(input("Enter student score (numeric value): ")) # Allows user to input student's score and converts it into an integer
        new_student = {'student_id': student_id, 'name': student_name, 'grade': student_grade, 'score': student_score} # Creates a dictionary with keys. 
        print(new_student)
        return new_student
    except ValueError: 
        print("Invalid input. Please enter a numeric score.") # If the user does not input a numeric score, it will prompt an error message
        return None
    
#7.4: Using a regular expression to check that a string matches a certain pattern
#7.5: You used regular expressions with groupings to extract or change parts of a string.
# Check name and grade
def check_name_and_grade(student):
    pattern = re.compile(r'^A.*?(\w)', re.IGNORECASE) 
    # Regular expression pattern is created using 're.compile'
    # The pattern 'r'^A.*?(\w)' is used to match a string that starts with 'A'. 
    # It captures the first word character
    # re.IGNORECASe is used to make the matching case-insensitive.
    match = pattern.match(student['name'] + student['grade']) # match is assigned to the result of applying 'pattern' to the student's nme and grade. Checks if it matches
    if match:
        first_letter = match.group(1) # If it is a match, this line will extract the first captured group and assign it to the variable
        print(f"Student {student['name']} starts with 'A' and the first letter of the grade is {first_letter}.")

# Main Program
initial_students = [ # 5.7:  Creating a list manually
    {'student_id': 1, 'name': 'Amy', 'grade': 'A', 'score': 90},
    {'student_id': 2, 'name': 'Bob', 'grade': 'B', 'score': 80},
    {'student_id': 3, 'name': 'Gerald', 'grade': 'C', 'score': 70}
]
new_student = {'student_id': 4, 'name': 'Billy', 'grade': 'A', 'score': 100} # 5.8: Appending a new student, Billy, to the list
initial_students.append(new_student)

print("Initial List of Students:") # Printing the initial list of students
print(initial_students)

# 8_2: Reading in a CSV of data into a data frame object using pandas 
# Change working directory
os.chdir(r"C:\Users\alexa\OneDrive\Final Project Coding - INST126") # Using a raw string to avoid needing to use backslashes
csv_file_path = "students.csv" # Specify the path to CSV file
students_df = pd.read_csv(csv_file_path) # read_csv is a function provided by Pandas for reading data from a CSV file

# Display the Original Students' data frame
print("Initial Students Data Frame:")
print(students_df)

# Clean the initial data frame
students_df = clean_dataframe(students_df)
    
# Allow users to input their own students
student_id = len(initial_students) + 1 # Calculates the new student ID by getting the length and adding 1. 
while True:
    new_student = get_user_input(student_id)
    if new_student is None:
        break
    initial_students.append(new_student) # Adds the information of the new student to the initial_students list
    check_name_and_grade(new_student) # The function checks if the student's name starts with 'A' 
    student_id += 1
    
#7.1: Using a string method to split a string into a list of smaller strings
#Allow users to input their own student names, separated by commas.
names_input = input("Enter student names (separated by commas: ") 
user_names = names_input.split(', ')
print("User inputted Names:", user_names)

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
        # Create a list of two arrays. The first array is the 'score' column and the second array is the result of applying a lambda function. 
        # The lambda function converts each letter grade (A to F) to a numeric value.
        [students_df['score'], students_df['grade'].apply(lambda x: ord(x) - ord('A') + 1)], # Each grade is converted to a numeric value
        axis=0, # The averaging is done along the first rows
        weights=[weight_score, weight_grade] # Provides the weights for the two arrays. weight_score = 0.9 and weight_grade = 0.1 
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
    deans_list_df = students_df[students_df['weighted_average'] > threshold] # Sets the students on the deans_list to those with a weighted average above the threshold
    return deans_list_df # Return the filtered data frame 

# Get the user's threshold 
user_threshold = float(input("Enter the threshold for the dean's list (numeric value): " )) # Prompt the user to set the threshold

# Filter students
deans_list_df = get_deans_list(final_students_df, user_threshold) # Call the function

# Dean's list with user's inputted threshold:
print("\n Dean's List with Threshold: ")
print(deans_list_df)

# 8_4: Writing the changed data to CSV using Pandas
deans_list_df.to_csv('deans_list.csv', index=False) #Uses the to_csv to write the contents to a CSV file. The index=false indicates that the DataFrame index should not be included in the file.
deans_list_from_csv = pd.read_csv('deans_list.csv') # Reads the contents of the CSV file into a new Data Frame
print("\n Dean's List from CSV: ")
print(deans_list_from_csv)
