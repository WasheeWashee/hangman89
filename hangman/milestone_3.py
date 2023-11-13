status = True
guess = input("Please guess a letter: ")

while status == True:
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        status = False
    else:
        guess = input("Invalid letter. Please, enter a single alphabetical character. ")
