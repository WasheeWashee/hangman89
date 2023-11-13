import random

word_list = ["Apple", "Banana", "Grapes", "Peaches", "Oranges"]
print(word_list)

word = random.choice(word_list)
print(word)

status = True
guess = input("Please guess a letter: ")

while status == True:
    if len(guess) == 1 and guess.isalpha():
        if guess.upper() or guess.lower() in word:
           print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
        status = False
    else:
        guess = input("Invalid letter. Please, enter a single alphabetical character. ")
