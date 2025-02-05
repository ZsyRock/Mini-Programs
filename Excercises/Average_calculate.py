sum_calculate = 0
input_index = 0

while True:  # Keep asking for input until "Q" is entered
    num_input = input("Please input any number as you wish, or press \"Q\" to quit: ")

    if num_input.upper() == "Q":  # Allow uppercase "Q" as well
        break  # Exit the loop

    try:
        num_input = float(num_input)  # Convert input to a float
        input_index += 1
        sum_calculate += num_input
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Calculate and print the average only if numbers were entered
if input_index > 0:
    average_calculate = sum_calculate / input_index
    print(f"The average of the entered numbers is: {average_calculate}")
else:
    print("No numbers were entered.")
