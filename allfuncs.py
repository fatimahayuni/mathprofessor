import random

def single_digits_sum():
    first_single_digit = random.randint(0,9)
    second_single_digit = random.randint(0,9)
    print(f"What is the sum of {first_single_digit} + {second_single_digit}?")
    sum_of_two_single_digits = first_single_digit + second_single_digit
    try:
        user_answer_string = input()

        user_answer_int = int(user_answer_string)
        if user_answer_int == sum_of_two_single_digits:
            print("Correct.")
        else:
            print("Try again.")
    except:
        print("Please enter an integer.")
    

def double_digits_sum():
    first_double_digit = random.randint(10,99)
    second_double_digit = random.randint(10,99)
    print(f"What is the sum of {first_double_digit} + {second_double_digit}?")
    sum_of_two_double_digits = first_double_digit + second_double_digit
    user_answer_string = input()
    user_answer_int = int(user_answer_string)
    if user_answer_int == sum_of_two_double_digits:
        print("Correct.")
    else:
        print("Try again.")

def triple_digits_sum():
    first_triple_digit = random.randint(100, 999)
    second_triple_digit = random.randint(100, 999)
    print(f"What is the sum of {first_triple_digit} + {second_triple_digit}?")
    sum_of_two_triple_digits = first_triple_digit + second_triple_digit
    user_answer_string = input()
    user_answer_int = int(user_answer_string)
    if user_answer_int == sum_of_two_triple_digits:
        print("Correct.")
    else:
        print("Try again.")

"""
1. If the answer is invalid (they entered 'one' instead of 1), then ask them to re-enter the integer and try again. 
I have used try/except for this before and I know this will work. I have always been confused between if-else and try/ecept so I will try to use if-else for this to understand 
this better and see if there's any difference. 
"""
        
