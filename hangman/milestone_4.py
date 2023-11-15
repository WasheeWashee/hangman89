import random

word_list = ["Apple", "Banana", "Grapes", "Peaches", "Oranges"]

class Hangman:
    def __init__(self, word_list, num_lives=None):
        self.word_list = word_list
        if num_lives == None:
            self.num_lives = 5
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for x in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        if guess.upper() in self.word or guess.lower() in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if guess.upper() == self.word[i] or guess.lower() == self.word[i]:
                    self.word_guessed[i] = guess.lower()
                    print(self.word_guessed)
                else:
                    pass
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        print(self.word)
        guess = input("Please guess a letter: ")
        status = True
        while status == True:
            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print("You already tried that letter!")
                    status = False
                    print(self.list_of_guesses)
                else:
                    Hangman.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    status = False
                    print(self.list_of_guesses)
            else:
                guess = input("Invalid letter. Please, enter a single alphabetical character: ")
