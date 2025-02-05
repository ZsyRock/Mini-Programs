try:
    housework_count = int(input("How many times have you done housework this month? "))
    red_envelope_count = int(input("How many red envelopes has your wife received this year? "))
    shopping_count = int(input("How many times have you bought gifts for your wife this year? "))
except ValueError:
    print("Input error! Please enter an integer.")
    exit()

is_angry_input = input("Is your wife happy today? (Enter 'T' for happy, 'F' for unhappy): ").strip().upper()
is_angry = is_angry_input == "F"

if housework_count >= 10 and red_envelope_count >= 1 and shopping_count >= 4 and not is_angry:
    print("Get ready for a Nintendo Switch!")
else:
    print("The Switch dream fades away...")
