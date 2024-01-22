import random

print("Guess the number: 1 - 100")
random_number = random.randint(1, 100)

# Test code...
# print(f"{random_number}")


def game_difficulty():
    """It is a function to set a difficulty for the game where you have a certain
     number of try's"""
    number_of_try = 0
    difficulty = input("Select the difficulty level: HARD or EASY: ").lower()
    if difficulty == "hard":
        number_of_try = 5
    elif difficulty == "easy":
        number_of_try = 10
    else:
        raise SystemExit("Invalid input. Try again...")
    print(f"You have {number_of_try} try's.")
    return number_of_try


def playing_the_game():
    """Here we determine if the player guessed the number and the remaining try's he has left."""
    lives = game_difficulty()
    player_guess = int(input("Guess the number: "))
    while player_guess != random_number:
        lives -= 1
        if lives == 0:
            print(f"You don't have anymore try's. You lose!")
            break
        if player_guess > random_number:
            print(f"You guessed too high. Try again... Lives remaining: {lives}")
        elif player_guess < random_number:
            print(f"You guessed too low. Try again... Lives remaining: {lives}")
        elif random_number == player_guess:
            print(f"You guessed right, the number is: {random_number}.")
        player_guess = int(input("Guess the number: "))


playing_the_game()