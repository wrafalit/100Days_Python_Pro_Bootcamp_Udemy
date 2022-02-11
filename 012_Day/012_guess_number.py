import random


def rand_num():
    num = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Below to hide a hint
    print("Pss the correct answer is ", num)
    return num


def difficulty():
    if (input("Choose a difficulty. Type 'easy' or 'hard': ")) == 'easy':
        guess = 10
    else:
        guess = 5
    print(f"You have {guess} attempts remaining to guess the number.")
    return guess


def make_guess():
    return int(input("Make a guess: "))


def check_guess_number(n, g):
    global game_off
    global guess
    if n == g:
        print("You Win")
        game_off = True
        return game_off
    elif n > g:
        print("Too low")
    else:
        print("Too high")
    guess -= 1
    if guess > 0:
        print("Guess again")
        print(f"You have {guess} attempts remaining to guess the number")

    return guess


game_off = False
num = rand_num()
guess = difficulty()
while not game_off:
    if guess > 0:
        user_guess = make_guess()
        guess = check_guess_number(num, user_guess)
    else:
        print("You've tun out of guesses, you lose")
        break
