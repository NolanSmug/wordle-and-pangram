Wordle and Pangram

This project contains two challenging and interactive word games, wordle and pangram. An explanation for the rules of each game are shown below.

Wordle:
The program selects a random 5 lettered word (hence why we import random). This is retrieved from the wordle_words.txt file, a list of 2,309 basic 5 letter english words. The goal is to guess this selected word by strategically guessing other 5 lettered words to make educated guesses about the secret word. The words you are allowed to guess are in a bigger 5 letter dictionary file (allowed_guesses.txt). To do so, for every guess the program will return 5 colored boxes each being either black(⬛️), yellow(🟨), or green(🟩). A black box indicates the letter in that spot is not in the secret word at all. A yellow box indicates the letter in that spot is in the word, however not in the spot you put it in. A green box indicates the letter in that spot is the same letter in the same spot in the secret word. The game also has a feature for displaying all of the letters in the alphabet that could be in the word by eliminating your previous incorrect guesses. This may make it easier for users to keep track of letters from previous guesses. This process is repeated a maximum of 6 times unless you guess the word earlier. When the game ends, the program prints an ordered grid/array of what colored boxes were returned upon each guess, which is a fun after-game summary to show your friends.

Pangram:
This game was heavily inspired by the New York Times Spelling Bee game. The program will give you a randomly generated list of 7 letters, 5 consonants and 2 vowels. The goal is to make as many words as you can using these letters, with some conditions:
	- One of the 7 letters (the letter printed first), must be used in every word.
	- You can repeat letters in the same word.
	- Words must be 4 or more letters.
	- 1 point gained for every letter (ex: 5 lettered word = 5 points, etc.)
To accomplish this, the program runs a function that iterates through a dictionary (dictionary.txt), and checks which words only contain the randomly generated letters (ignoring < 3 lettered words). The game ends when the user finds every word possible (a difficult task), or when the user inputs 'ext', to which the program prints all the possible words that the user missed.

How to run:
When the program is ran in an IDE, it first prompts for which game you want to play (w for wordle, p for pangram). Depending on the user's choice, that game is then executed in the shell.
