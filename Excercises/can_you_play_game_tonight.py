try:
    mood_index = int(input("Enter your wife's mood index today (0-100): "))
except ValueError:
    print("Input error! Please enter an integer between 0 and 100.")
    exit()

at_home_input = input("Is she at home? (Enter 'T' for yes, 'F' for no): ").strip().upper()
at_home = at_home_input == "T"

play_game = "Time to play games! Haha, let's go!"
dont_play = "For the sake of your life, better not play!"

if not at_home:
    print(play_game)
elif mood_index >= 60:
    print(play_game)
else:
    print(dont_play)
