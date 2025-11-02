# import numpy as np
# import pandas as pd

# np.random.seed(42)

# ids = np.arange(1, 11)
# ages = np.random.randint(18, 60, 10)
# salaries = np.random.randint(30000, 90000, 10)
# departments = np.array(["HR", "IT", "Finance", "IT", "HR", "Sales", "Finance", "IT", "Sales", "HR"])

# DF = pd.DataFrame({
#   "id": ids,
#   "age": ages,
#   "salary": salaries,
#   "dept": departments
# })

# DF.to_csv("employees.csv", index=False)
# print("Sample Data Created and Saved as employees.csv")

# table

# id,age,salary,dept
# 1,56,77191,HR
# 2,46,74131,IT
# 3,32,46023,Finance
# 4,25,71090,IT
# 5,38,31685,HR
# 6,56,30769,Sales
# 7,36,89735,Finance
# 8,40,86101,IT
# 9,28,32433,Sales
# 10,28,35311,HR

# 1) NumPy — 5 Questions
# Q1. Create NumPy arrays from the ages and salaries data generated above. Print both arrays and display their dtype, ndim, shape, and size.
# Q2. Using the salaries array, find and print the highest and lowest salary values. Also, calculate and print the average salary and age using NumPy functions.
# Q3. From the ages array, filter and print all ages greater than 30 using a boolean condition. Then count and print how many employees are older than 30.
# Q4. Create a new NumPy array that increases every employee’s age by 5 years (without modifying the original array). Print the new updated ages array.
# Q5. Using NumPy, calculate the total salary expense (sum of all salaries) and the difference between the maximum and minimum salary. Print both results.

# 2) Pandas — 5 Questions
# Q6. Load the employees.csv file into a Pandas DataFrame. Display the first 5 rows, and check basic info using info() and summary statistics using describe().
# Q7. Display only the id, age, and salary columns. Then show the last 3 rows using tail().
# Q8. Filter the DataFrame to show only employees who work in the IT department. Print the result and show the total number of IT employees.
# Q9. Sort the DataFrame by salary in descending order and display the top 3 highest-paid employees along with their department and age.
# Q10. Replace all salary values greater than 80000 with 80000 using loc. Then calculate and print the new average salary of all employees after replacement.


# questions 1
import numpy as np

ages = np.array()
