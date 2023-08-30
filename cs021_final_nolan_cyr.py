"""
Final Project
Wordle and Pangram
Nolan Cyr
"""

import random


def pangram():
    def possible_words(letters):
        """
        Takes dictionary.txt file and iterates through every word
        searching for each word that only contains 4 or more of the
        randomly generated letters
        """
        with open('dictionary.txt','r') as f:
            words_lst = []
            for word in f:
                words_lst.append(word.strip('\n'))
            f.close()

        letterArray = list(letters)
        possible_words_lst = []

        for word in words_lst:
            if len(word) > 3:
                match = True
                matchCount = 0
                letterArray = list(letters)
                for i in range(0, len(word)):
                    if letters.find(word[i]) == -1:
                        match = False
                        break

                    if word[i] in letterArray:
                        for x in range(7):
                            if letterArray[x] == word[i]:
                                letterArray[x] = ''
                        matchCount += 1

                if match and word.find(letters[0]) != -1:
                   possible_words_lst.append(word)

        return possible_words_lst


    def possible_points(lst):
        """
        Calculates total points possible based
        on possible words
        """
        points = 0
        for word in lst:
            points = points + len(word)

        return points


    CONSONANTS = ['B', 'C', 'D', 'F', 'G', 'H', 'K',
                  'L', 'M', 'N', 'P', 'R', 'S', 'T',
                  'Y']

    VOWELS = ['A', 'E', 'I', 'O', 'U']


    # Choosing letters randomly
    chosen_letters = []
    needed_letter = random.choice(CONSONANTS)
    CONSONANTS.pop(CONSONANTS.index(needed_letter))
    chosen_letters.append(needed_letter)

    for i in range(4):
        consonant = random.choice(CONSONANTS)
        CONSONANTS.pop(CONSONANTS.index(consonant))
        chosen_letters.append(consonant)
        
    for i in range(2):
        vowel = random.choice(VOWELS)
        VOWELS.pop(VOWELS.index(vowel))
        chosen_letters.append(vowel)

    print("Type 'ext' to quit")

    chosen_letters = ''.join(chosen_letters)
    possible_words = possible_words(chosen_letters)

    # print(f'\n{possible_words}') #printing answers for testing purposes

    guess = ''
    score = 0
    gameover = False
    already_guessed = []
    total_words = len(possible_words)
    total_points = possible_points(possible_words)
    print(f'\nTotal words: {total_words}')
    print(f'Possible points: {total_points}\n')

    while score < total_points and not gameover:
        print('  '.join(chosen_letters))
        guess = input(f'Enter a 4+ letter word (you must use the letter'
                      f' {needed_letter}): ').upper()

        if ((guess in possible_words) and (needed_letter in guess)
        and (guess not in already_guessed)):
            score = score + len(guess)
            already_guessed.append(guess)
            print(f'\nYou got {len(guess)} points!')
            print(f'{len(already_guessed)} out of {total_words} words found.')
            print(f'Current Score: {score}\n')

        elif guess in already_guessed:
            print('Already guessed!\n')

        elif guess == 'EXT':
            gameover = True
            
        elif guess not in possible_words:
            print('Invalid word!\n')

    print('\nGAME OVER')
    print('---------')
    print("Correctly guessed words:")
    print(already_guessed)

    print("\nAll possible answers:")
    print(possible_words)
    
    print(f'\nYour score: {score} out of a possible {total_points} points.')






def wordle():
    #reading word files
    with open('wordle_words.txt', 'r') as f:
        words_lst = []
        for word in f:
            words_lst.append(word.strip('\n'))
        f.close()


    with open('allowed_guesses.txt', 'r') as f:
        guesses_lst = []
        for word in f:
            guesses_lst.append(word.strip('\n'))
        f.close()

    #setting variables for printing
    WRONG_LETTER = '⬛️'
    RIGHT_LETTER = '🟨'
    RIGHT_SPOT   = '🟩'
    SECRET_WORD = words_lst[random.randint(0, len(words_lst))]
    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']


    #print(SECRET_WORD) #printing answer for testing purposes

    #game start (all empty letters)
    for i in range(5):
        print(f'{WRONG_LETTER}',end = '')

    #setting up guess info
    guess = ''
    guess_history = []
    guess_count = 6

    while guess != SECRET_WORD and guess_count > 0:
        guess_pattern = [WRONG_LETTER,WRONG_LETTER,WRONG_LETTER,WRONG_LETTER,WRONG_LETTER] #initialize guess to all black
        guess = input('\n\nEnter a 5 letter word'
                        '(? to see unused letters): ',).lower()
        #if you win:
        if guess == SECRET_WORD:
            guess_history.append(RIGHT_SPOT+RIGHT_SPOT+RIGHT_SPOT+RIGHT_SPOT+RIGHT_SPOT)

        elif guess in guesses_lst:
            secret_word_lst = list(SECRET_WORD) #turning secret word into a list

            #check all spots for green space first (in case of more than 1 correct letter)
            for letter in range(5):

                if guess[letter] == secret_word_lst[letter]:
                    guess_pattern[letter] = RIGHT_SPOT
                    secret_word_lst[letter] = ''
                    #temporarily removing letter to deal with duplicate letter case

            #check for yellows (ignore if already green)
            for letter in range(5):
                
                if guess[letter] in secret_word_lst:
                    if guess_pattern[letter] != RIGHT_SPOT: #ignore spot if it's already green
                        guess_pattern[letter] = RIGHT_LETTER
                        index = secret_word_lst.index(guess[letter])
                        secret_word_lst[index] = ''
                        #temporarily removing letter to deal with duplicate letter case

            #remove letters from 'letters can guess'
            for letter in range(5):
                if guess[letter] not in SECRET_WORD:
                    if guess[letter] in ALPHABET:
                        ALPHABET.remove(guess[letter])
                    
            guess_count = guess_count - 1
            print(''.join(guess_pattern))
            guess_history.append(''.join(guess_pattern))
            print(f'\nGuesses left: {guess_count}')

        elif guess == '?':
            print(f'\nLetters you can use:\n\n{ALPHABET}')

        else:
            print('Invalid word!')

    if guess_count == 0:       
        print(f'\nYOU LOSE! The word was {SECRET_WORD.upper()}')
    else:
        print('You got it!')
        
    print(f'\nGame summary:')
    for guess in guess_history:
        print(guess)
        
    
if __name__ == '__main__':

    game = ''
    
    while game != 'w' and game != 'p':
        game = input('Do you want to play wordle or pangram?'
                     '(w for wordle, p for pangram): ').lower()

        if game == 'w':
            print('\n')
            wordle()

        elif game == 'p':
            print('\n')
            pangram()
