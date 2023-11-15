# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Table of Contents
1. Description of the project
2. Usage instructions
3. Installation instructions (None)
4. File structure
5. License information (None)

## Description
In this project, we have aimed to recreate the classic game of Hangman, where the computer thinks of a word and the user tries to guess it, one letter at a time. It is coded using Python, using Object Oriented Programming to create a class containing attributes and methods that asks the user for guesses, validates them, and checks whether they are in the code. A "while loop" is then used to iterate through the rest of the rounds, ending the game when the player either fully guesses the word, or they run out of lives.

## Usage Instructions
In order to start the game, please enter play_game() into the terminal, passing a list of words of the user's choice as the argument. For example, if the user wanted the computer to select a random word from the list: apple, banana, grape, peach, orange, they would enter play_game(["apple", "banana", "grape", "peach", "orange"]). Upon doing so, the program will ask for an initial guess. If the guessed letter is contained within the target word, then a message congratulating the player on their guess will appear, showing the position of the letter in the word. Should the guessed letter not be within the target word, then a similar commiserative message will appear, and the player will lose a life. In both cases, a list of previously guessed letters will be shown to aid the player, so that they don't guess the same letter. Should they do so, or enter an unsuitable guess, a corresponding message will appear asking the player to try again. The game is won when the player guesses all of the letters in the word before losing all of their lives, and lost when they lose all of their lives before guessing the word completely.

## File Structure
Within the file, there are 4 milestones: milestone_2, milestone_3, milestone_4 and milestone_5. These show the gradual development and progression of the project as more and more features were added, according to the AiCore guidelines. 
