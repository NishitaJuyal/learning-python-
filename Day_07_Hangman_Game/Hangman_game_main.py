import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
print(logo)

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
all_guesses = []
while not game_over:

    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    all_guesses.append(guess)


    display = ""
    if guess in correct_letters:
        print(guess)
        print(f"You've already guessed {guess}")
    if guess in all_guesses:
        print(guess)
        print(f"You've already guessed {guess}")


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.\n YOU LOSE A LIFE.")

        if lives == 0:
            game_over = True
            print(f"IT WAS {chosen_word}. GAME OVER)")
            print("**********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
