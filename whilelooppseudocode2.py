while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        # Better try again...return to the start of the loop. 
        continue
    else:
        # age was successfully parsed!
        # we are ready to exit the loop.
        break

if age >= 18:
    print("You are able to vote!")
else:
    print("You are NOT able to vote.")