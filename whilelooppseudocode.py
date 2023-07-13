while True:
    play_an_awesome_game()

    answer = input("Play again, Yes(y) or no(n)?:")
    
    if answer == "n":
        print("Ok, we're done.")
        break
    
    print("We go again...")