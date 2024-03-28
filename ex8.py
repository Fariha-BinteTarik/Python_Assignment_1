def guessing_game():
    secret_num = 6 
    user_input = input("Guess the number between 1 and 9: ")
    
    try:
        guess = int(user_input)
        if guess < secret_num:
            print("Your guess is almost there.")
        elif guess > secret_num:
            print("Your guess is higher.")
        else:
            print("Your guess is correct!")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 9.")

guessing_game()
