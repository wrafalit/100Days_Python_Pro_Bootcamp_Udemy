import random
import hangman_words
import hangman_art

print(hangman_art.logo)
word_list = hangman_words.word_list
lives = 6
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}')


display = []
for ch in chosen_word:
    display.append('_')

game_end = False

while not game_end:
    print(display)
    print(hangman_art.stages[lives])
    guess = input("Guess a letter? ").lower()
    for ch in range(len(chosen_word)):
        if chosen_word[ch] == guess:
            if guess not in display:
                display[ch] = guess
            else:
                print("You have already guessed ", guess)
    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed a {guess} that is not in word, you lose a life!')
        if lives == 0:
            game_end = True
            print("You lose!")
    if "_" not in display:
        game_end = True
        print("You Win")