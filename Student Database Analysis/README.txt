# Final Project - Student Database Analysis

# Overview
This project involves analyzing a student data base to calculate the weighted average scores for each students and identify which students qualify for the dean's list.

## Project Structure:
- 'students.csv': CSV file containing the student database.
- 'deans_list.csv': CSV file containing the list of students on the dean's list.

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
- Prompts the user to set a threshold for identifying studnets on the Dean's List.

# 9. Regular Expression
- A regular expression is employed to check if a student's name starts with 'A'. 
- Regular expressions are used to extract parts of a string.

## How to Use
1. Clone the repository.
2. Ensure you have the required dependencies installed (`pip install pandas numpy matplotlib`).
3. Run the script: `python final_project.py`
4. Input any user input (ie: student name, grade, score) 

## Author
Alexa Chu

## License
This project is licensed under the [MIT License](LICENSE). 
