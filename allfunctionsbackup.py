import random

def single_digits_sum():

    # Create 2 random integers, and then add them up. Create 10 sums.
    for x in range(10):
        first_single_digit = random.randint(0,9)
        second_single_digit = random.randint(0,9)
        print(f"What is the sum of {first_single_digit} + {second_single_digit}?") # starts here
        sum_of_two_single_digits = first_single_digit + second_single_digit

        # A user might enter a wrong answer at this block. Like "ten" instead of "10".
        try:

            # User enters an input which is in string format. This string format is then converted to an integer. 
            user_answer_string = input()
            user_answer_int = int(user_answer_string)

            # If the user enters the correct answer to the sum, the program will print "Correct."
            if user_answer_int == sum_of_two_single_digits:
                print("Correct.")
                print()

            # If the user enters the wrong answer to the sum, the program will give the user 2 more attempts.
            else:
                print()
                print("Try again. You have 2 more attempts.")
                count = 0
                while count < 2:
                    answer_again_string = input("Answer: ")
                    answer_again_int = int(answer_again_string)
                    if answer_again_int == sum_of_two_single_digits:
                        print("You got it right at the second attempt!")
                        break
                    else:
                        print("Wrong again.")
                        print()
                        count += 1
        
        
        # If the user enters a wrong answer like "one" instead of "1", this block will be triggered. 
        except: 
            except_block_user_answer_string = input("Please enter an integer like '1' instead of 'one': ")
            except_block_user_answer_int = int(except_block_user_answer_string)

            # If the user finally enters an integer instead of a string, this block is triggered: 
            if except_block_user_answer_int == sum_of_two_single_digits:
                print("Correct.")
                print()
            else:
                print("Try again.")
                print()

def double_digits_sum():
    for x in range(10):
        first_double_digit = random.randint(10,99)
        second_double_digit = random.randint(10,99)
        print(f"What is the sum of {first_double_digit} + {second_double_digit}?")
        sum_of_two_double_digits = first_double_digit + second_double_digit
        user_answer_string = input()
        user_answer_int = int(user_answer_string)
        if user_answer_int == sum_of_two_double_digits:
            print("Correct.")
            print()
        else:
            print("Try again.")
            print()

def triple_digits_sum():
    for x in range(10):
        first_triple_digit = random.randint(100, 999)
        second_triple_digit = random.randint(100, 999)
        print(f"What is the sum of {first_triple_digit} + {second_triple_digit}?")
        sum_of_two_triple_digits = first_triple_digit + second_triple_digit
        user_answer_string = input()
        user_answer_int = int(user_answer_string)
        if user_answer_int == sum_of_two_triple_digits:
            print("Correct.")
            print()
        else:
            print("Try again.")
            print()

    
"""
TASKS for 10th FEB 2023:
What is 1 + 2?: 5
Incorrect - you have 2 attempts remaining.

What is 1 + 2?: 6
Incorrect - you have 1 attempt remaining.

What is 5 + 2?: 7
Incorrect - you have failed this round.
Next round.

--------------------------
If the user keeps entering invalid input like "eleven" instead of "11", no limit for how many times she can try. keep asking until she enters an integer. 

If they do not guess the number within 3 valid attempts, record that they failed the round and go to the next round (new sum). 

If the answer is correct, you go to the next round recording that they successfully got this round correct <-- empty list. populate with the word 'correct' and the opposite. 

After 10 rounds, report to the user how many rounds they got right, and how many they failed <--- empty list. populate with the word 'correct' and 'wrong'. 

After reporting the game result, the game will restart asking for a level to play.

The game must start in a function named "main", which should be called when running the Python file to begin the game.

Here's the example output:


Round 1
What is 5 + 2?: Red
Invalid input - try again.

What is 5 + 2?: 5
Incorrect - you have 2 attempts remaining.

What is 5 + 2?: 9
Incorrect - you have 1 attempt remaining.

What is 5 + 2?: 7
Correct! Next round.

Round 2
What is 9 + 1?: 10
Correct! Next round.

Round 3:
What is 1 + 2?: 5
Incorrect - you have 2 attempts remaining.

What is 1 + 2?: 6
Incorrect - you have 1 attempt remaining.

What is 5 + 2?: 7
Incorrect - you have failed this round.
Next round.

...
etc.
...
You have now completed all 10 rounds.
You got 7 rounds correct.
You got 3 rounds incorrect.

Lets play again.

Choose a level between 1 and 3:

"""