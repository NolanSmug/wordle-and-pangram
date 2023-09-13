# Wordle and Pangram Games

This project contains two challenging and interactive word games: Wordle and Pangram. Below are the explanations for the rules of each game.

## Wordle

The program selects a random 5-lettered word (hence why we import random). This is retrieved from the `wordle_words.txt` file, a list of 2,309 basic 5-letter English words. The goal is to guess this selected word by strategically guessing other 5-lettered words to make educated guesses about the secret word. The words you are allowed to guess are in a bigger 5-letter dictionary file (`allowed_guesses.txt`). 

To do so, for every guess the program will return 5 colored boxes each being either black(⬛️), yellow(🟨), or green(🟩). 
- A black box indicates the letter in that spot is not in the secret word at all. 
- A yellow box indicates the letter in that spot is in the word, however not in the spot you put it in. 
- A green box indicates the letter in that spot is the same letter in the same spot in the secret word.

The game also has a feature for displaying all of the letters in the alphabet that could be in the word by eliminating your previous incorrect guesses. This may make it easier for users to keep track of letters from previous guesses. This process is repeated a maximum of 6 times unless you guess the word earlier. When the game ends, the program prints an ordered grid/array of what colored boxes were returned upon each guess, which is a fun after-game summary to show your friends.

## Pangram

This game was heavily inspired by the New York Times Spelling Bee game. The program will give you a randomly generated list of 7 letters, 5 consonants and 2 vowels. The goal is to make as many words as you can using these letters, with some conditions:
- One of the 7 letters (the letter printed first), must be used in every word.
- You can repeat letters in the same word.
- Words must be 4 or more letters.
- 1 point gained for every letter (ex: 5 lettered word = 5 points, etc.)

To accomplish this, the program runs a function that iterates through a dictionary (`dictionary.txt`), and checks which words only contain the randomly generated letters (ignoring < 3 lettered words). The game ends when the user finds every word possible (a difficult task), or when the user inputs 'ext', to which the program prints all the possible words that the user missed.

## How to Run

To get started with the Wordle and Pangram games, follow these steps:

1. **Download the Project Files:**
   - Ensure you have downloaded all the necessary project files, including `wordle_words.txt`, `allowed_guesses.txt`, and `dictionary.txt`.

2. **Open in IDE:**
   - Open the project folder in your preferred Integrated Development Environment (IDE).

3. **Choose the Game:**
   - In your IDE, execute the main program.
   - The program will prompt you to choose a game:
     - Type `w` for Wordle or `p` for Pangram and press Enter.

4. **Enjoy the Game:**
   - Follow the on-screen instructions to play the selected game.

5. **Have Fun!**
   - Engage in the challenge of guessing the secret word in Wordle or creating words in Pangram.

Feel free to explore and enjoy both games! If you have any questions or need further assistance, don't hesitate to reach out.

## Contact
For any inquiries or issues, please contact [Nolan Cyr](mailto:nolangcyr@gmail.com)
