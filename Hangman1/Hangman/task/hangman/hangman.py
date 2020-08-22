import random
import string


def hangman():
    count = 8                                                           # count starts from 8
    word = random.choice(['python', 'java', 'kotlin', 'javascript'])    # Word list for the game
    word_dict = dict()                            # empty dictionary to keep indexes of each letter occuring in a word
    letters = []
    guess = ['-' for _ in range(len(word))]       # initial ---- 'dashed word'

    for i in word:
        if i not in word_dict:                    # if the letter is not present then create a key of that letter
            word_dict[i] = [word.index(i)]        # the first index of the occuring letter is the corresponding value
        else:
            last_index = word_dict[i][-1]         # if word is already there then append to the existing list of indexes
            word_dict[i].append(word[last_index + 1:].index(i) + last_index + 1)
            # as index returns the first occurance so the search starts after the last occurance of the word
        
    print('H A N G M A N \n')                               # Just the haeding of the game

    while count > 0:                                        # as only 8 tries are given
        print(''.join(guess))                               # for stringing together the '-' dashes in the guess
        letter = input('Input a letter: ')                  # Taking user input or the 'guess' from the user

        if len(letter) != 1:
            print('You should input a single letter\n')     # if a single character is not entered
            continue
        if letter not in string.ascii_lowercase:            # if the character entered is not a lowercase letter
            print('It is not an ASCII lowercase letter\n')
            continue

        if letter not in letters:                           # to keep track of the letters already used by the user
            letters.append(letter)

            if letter in word:                              # checking if the 'guess' is in the chosen word
                for p in range(len(word_dict[letter])):     # replacing as many times as the letter occurs in the word
                    guess[word_dict[letter][p]] = letter    # the word_dict[letter] contains the list of the indices

                    if '-' not in guess:                    # if there are no blanks ('-') remaining
                        print('You guessed the word!', 'You survived!', sep='\n')
                        break
                print('')                                   # blank line required to comply with the format of the game
            else:
                print('No such letter in the word')         # if no letter is found then this is displayed
                count -= 1
                if count != 0:                              # list of 'used' letters
                    print('\n')
        else:
            print('You already typed this letter')
            if count != 0:
                print('\n')

    if count == 0:
        print('You are hanged!\n')                          # after the game is over this is the ending phrase


while True:                                                 # For continuous play
    command = input('Type "play" to play the game, "exit" to quit: ')
    if command == 'play':
        hangman()
    elif command == 'exit':
        break
