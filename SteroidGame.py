from allfunctions import *


print()
chosen_level = input("Choose a level between 1 and 3: ")
if chosen_level == "1":
    print("You have chosen Level 1.")
    print()
    single_digits_sum()
elif chosen_level == "2":
    double_digits_sum()
elif chosen_level == "3":
    triple_digits_sum()
else:
    input("Please enter number between 1-3: ")
print()
