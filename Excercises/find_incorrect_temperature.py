import random

# Create an empty dictionary employee_temperatures to store employee IDs (keys) and body temperatures (values).
employee_temperatures = {}

''' Generate employee IDs and random body temperatures for 100 employees.
str(i): Converts i to a string (e.g., 1 → "1").
.zfill(4): Ensures the string is 4 digits long, padding with zeros if necessary (e.g., "1" → "0001", "12" → "0012").
f"EMP{...}": Uses f-string formatting to generate employee IDs like "EMP0001", "EMP0002", ..., "EMP0100".
'''
random.seed(666)

for i in range(1, 101):  # From 1 to 100
    employee_id = f"EMP{str(i).zfill(4)}"  # Generate employee IDs like EMP0001, EMP0002, etc.

    '''random.uniform(36.0, 38.5) generates a random floating-point number between 36.0 and 38.5 (simulating real body temperature).
round(..., 1) keeps one decimal place to ensure consistent data formatting (e.g., 37.2, 36.8).'''

    temperature = round(random.uniform(36.0, 38.5), 1)  # Generate random temperature and format to 1 decimal place.
    employee_temperatures[employee_id] = temperature  # Add employee ID and temperature to the dictionary.
# high_temp_employees = {emp_id: temp for emp_id, temp in employee_temperatures.items() if temp > 37.5}
#
# print("Employees with a temperature above 37.5°C:")
# print(high_temp_employees)
high_temp_employees = {}

for emp_id, temp in employee_temperatures.items():
    if temp > 37.5:
        high_temp_employees[emp_id] = temp

print("Employees with a temperature above 37.5°C:")
print(high_temp_employees)