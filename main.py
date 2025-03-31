import random
import time

print("Welcome to HANGMAN!")
print("Guess the letters of the word correctly.")
print("The words are Fruity ;) 🍒🍏")
print("MAY THE ODDS BE IN YOUR FAVOR!!")

SomeWords = ['apple', 'mango', 'banana', 'guava', 'litchi', 'orange', 'grape', 'strawberry', 'blueberry', 'pineapple', 'papaya', 'avocado']
chosen = random.choice(SomeWords)
play = list(chosen)
n = len(play)

time.sleep(2)

GuessWord = play[1:n-1]  

hidden_word = [play[0]] + ["_"] * (n - 2) + [play[-1]]
print("\nWord to guess:", " ".join(hidden_word))


guessed_letters = set()
attempts = n

while "_" in hidden_word and attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter. Try a different one.")
        continue

    guessed_letters.add(guess)

    if guess in GuessWord:  
        print("Correct Guess!")
        for i in range(1, n - 1):  
            if play[i] in GuessWord and play[i] == guess:  
                hidden_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

    print("Word:", " ".join(hidden_word))
    print(f"Attempts left: {attempts}")

if "_" not in hidden_word:
    print("\nYou Guessed Correctly 🎊🥳🎉🍾")
    print("Congratulations! You guessed the word:", chosen)
else:
    print("\nGame Over! The word was:", chosen)
