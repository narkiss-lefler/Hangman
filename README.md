# Hangman
In this program we will implement a variation of the game "Hangman". The goal of the game is to correctly guess a word or
phrase chosen by one of the players by guessing the letters that make them up.

In the first step, one of the players chooses a word, and writes horizontal lines next to each other as the number of letters.
The other player guesses letters: if the letter he guessed appears in the word chosen by the first player, 
then the player reveals the letter in all the places where it appears. If the guessed letter is wrong, 
the first player draws one part of a hanging pole with a person hanging on it and writes the wrong letter on the side. 
The guessing player must succeed in guessing the word before the first player completes the hanging pole.
#
In the game we assume the following conditions:
- The word that needs to be guessed is one and consists only of letters that are lower case.
- The letters in the template that are not visible will be represented by the character _ (underline).
- The pattern, word and letters are represented as strings.
- The player can choose to guess one letter from the pattern, or the full word.
- A player is assigned a number of points at the beginning of each round of games.
   Each guess costs him a point, but he can earn extra points if the guesses are correct.
- The player can ask for a hint that offers him possible words for the solution, each request for a hint costs the player a point.
- We will not draw a hanging pole, unlike the original game. 😬
#

## Part A
In the part the computer chooses randomly a word and the user tries to figure it out.
After the game ends,                                    
the player can choose to play the game again and again.              
At this point the list of incorrect guesses is empty, the length of the pattern is the length of the word,               
and all its letters are not visible.

progress of the game:
1. We will display the current state by calling **display_state**
2. We will receive the input from the user by calling **get_input**
3. If the input is a guess of a letter we will perform the following actions:
   - If the input is not correct, that is, its length is greater than one or is not a letter,
     or is not a lowercase letter, the message parameter is set to the user with a message indicating that the input is not correct and       we move to the next round.
   - If the chosen letter has already been chosen before, a message indicating this will be issued and then we will move on        to         the next round
   - Otherwise, we will deduct one point for the user.                            

The game ends when the pattern is fully revealed, or the player's score is 0. Otherwise, we continue to another round of the game.    
At the end of a game, a message will appear and the number of points will be reset.
After the game is over the player can choose to play another game. If he won the last game, the amount of positive points continues
with him to the next round.
#






  
