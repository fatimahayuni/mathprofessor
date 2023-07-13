print("Enter the correct username and password combo to continue")
count = 0
while count < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if password == "BTS" and username == "haslindahalim":
        print("Access granted")
        break
    else:
        print("Access denied. Try again.")
        print()
        count += 1