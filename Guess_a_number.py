import random

print("Guess the number: 1 - 100")
random_number = random.randint(1, 100)
random_number_lvl2 = random.randint(1, 200)


# Test code...
# print(f"{random_number}")
# print(f"{random_number_lvl2}")

def choose_level():
    level_options = input(f"Choose a level you want to play: level [1] - [1:100] or level [2] - [1:200]: ")
    if level_options == "1":
        return random_number
    elif level_options == "2":
        return random_number_lvl2
    else:
        raise SystemExit("Invalid input. Try again...")


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


def restarting():
    """Option for the player to replay the game if they want again."""
    restart_or_not = input("Do you want to play again? [Y]es or [N]o: ").lower()
    if restart_or_not == "y":
        return playing_the_game()
    else:
        raise SystemExit("Thank you for playing.")


def playing_the_game():
    """Here we determine if the player guessed the number and the remaining try's he has left."""
    levels = choose_level()
    lives = game_difficulty()
    player_guess = int(input("Guess the number: "))
    while player_guess != levels:
        lives -= 1
        if lives == 0:
            print(f"You don't have anymore try's. You lose!")
            break
        if player_guess > levels:
            print(f"You guessed too high. Try again... Lives remaining: {lives}")
        elif player_guess < levels:
            print(f"You guessed too low. Try again... Lives remaining: {lives}")
        elif levels == player_guess:
            print(f"You guessed right, the number is: {levels}.")
        player_guess = int(input("Guess the number: "))


playing_the_game()
restarting()
