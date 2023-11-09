#################################################################
"""In this program we will implement a variation of the game "hangman".
The goal of the game is to correctly guess a word or phrase chosen by
one of the players by guessing the letters that make them up."""
#################################################################

import hangman_helper

def starting_pattern(word):
    """function that gives the starting pattern"""
    for i in range(len(word)):
        return "_" * len(word)

################## PART B CHECKS #############################

def rule_1(words, pattern, ):
    """for the clues, we want to filter all the words that are:
     The same length of the pattern that the player create to this point."""
    filter_lst1 = []
    for i in range(len(words)):
        if len(words[i]) == len(pattern):
            filter_lst1.append(words[i])
        else:
            continue
    return filter_lst1


def rule_2(words, pattern, wrong_guess_lst):
    """for the clues, we want to filter from filter_lst1 all the words
    that are: don't contain any letter that appears in the list of
     incorrect guesses."""
    filter_lst2 = []
    filter_lst1 = rule_1(words, pattern)
    for i in range(len(filter_lst1)):
        sum2 = 0
        for j in range(len(filter_lst1[0])):
            if filter_lst1[i][j] not in wrong_guess_lst:
                sum2 += 1
                if sum2 == len(filter_lst1[0]):
                    filter_lst2.append(filter_lst1[i])
            else:
                break
    return filter_lst2


def rule_3(words, pattern, wrong_guess_lst):
    """for the clues, we want to filter from filter_lst2 all the words
    that are: contain identical letters in exactly the same positions of the
     letters visible in the pattern and that these letters are not found
     elsewhere in the filtered word"""
    char = len(pattern) - pattern.count("_")
    filter_lst3 = []
    filter_lst2 = rule_2(words, pattern, wrong_guess_lst)
    for i in range(len(filter_lst2)):
        sum3 = 0
        for j in range(len(filter_lst2[0])):
            if pattern[j] != "_":
                if filter_lst2[i][j] == pattern[j]:
                    sum3 += 1
            if ((filter_lst2[i][j] != pattern[j]) and (filter_lst2[i][j]
                in pattern)):
                sum3 -= 1
        if sum3 == char:
            filter_lst3.append(filter_lst2[i])
    return filter_lst3


def filter_words_list(words, pattern, wrong_guess_lst):
    """function return the full filtered list after 3 different filter rules"""
    filter_list = rule_3(words, pattern, wrong_guess_lst)
    return filter_list


def hint_length(words, pattern, wrong_guess_lst):
    """the function returns the list of hints filtered, with the length of the
     HINT_LENGTH value in the required indexes"""
    hint_list = filter_words_list(words, pattern, wrong_guess_lst)
    final_hint_length = [hint_list[0]]
    x = 1
    n = len(hint_list)
    num = hangman_helper.HINT_LENGTH
    for j in range(num - 1):
        i = (n * x) // num
        final_hint_length.append(hint_list[i])
        x += 1
    return final_hint_length


#############################################


def run_single_game(words_list, score):
    """The function runs one round of the game, until the player discovers
     the random word himself, or run out of points"""
    word = hangman_helper.get_random_word(words_list)
    pattern = starting_pattern(word)
    wrong_guess_lst = []

    msg = "single game started, good luck!"

    while score > 0 and '_' in pattern:
        hangman_helper.display_state(pattern, wrong_guess_lst, score, msg)
        (choice, input) = hangman_helper.get_input()

        if choice == hangman_helper.LETTER:
            letter = input
            if len(letter) != 1 or not letter[0].islower():
                msg = "The letter is not valid"
                continue
            if letter in wrong_guess_lst:
                msg = "you already tried this letter"
                continue
            if letter in pattern:
                msg = "you already tried this letter"
                continue

            score -= 1
            if letter in word:
                pattern = update_word_pattern(word, pattern, letter)
                n = word.count(letter)
                bonus_score = n * (n + 1) // 2
                score += bonus_score
                msg = "correct guess, you got " + str(bonus_score) + \
                      " bonus score"
            else:
                wrong_guess_lst.append(letter)
                msg = "wrong guess"

        elif choice == hangman_helper.WORD:
            score -= 1
            if input == word:
                n = pattern.count("_")
                bonus_score = n * (n + 1) // 2
                score += bonus_score
                msg = "correct word you won, you got " + str(bonus_score) + \
                      " bonus score"
                pattern = word
            else:
                msg = "the word is an incorrect guess"
        elif choice == hangman_helper.HINT:
            msg = "got a hint for help!"
            score -= 1
            hint_list = filter_words_list(words_list, pattern, wrong_guess_lst)
            matches = hint_length(words_list, pattern, wrong_guess_lst)
            if len(hint_list) > hangman_helper.HINT_LENGTH:
                hangman_helper.show_suggestions(matches)
            else:
                hangman_helper.show_suggestions(hint_list)

    if '_' in pattern:
        msg = "you lose, the word was " + word
    else:
        msg = "you win!"
    hangman_helper.display_state(pattern, wrong_guess_lst, score, msg)
    return score


def run_multiple_games(words):
    """The function counts the number of games the player played and checks
     if he is interested in another game"""
    points = hangman_helper.POINTS_INITIAL
    num_games = 0


    while True:
        points = run_single_game(words, points)
        num_games += 1
        if points > 0:

            msg = "you played " + str(num_games) + " with score of " \
                  + str(points) + " points, wanna play another round?"

            if hangman_helper.play_again(msg):

                continue
            else:
                break
        else:
            msg = "you survived " + str(num_games) + " game, wanna play again?"
            num_games = 0
            if hangman_helper.play_again(msg):
                points = hangman_helper.POINTS_INITIAL
            else:
                break


def main():
    """the function that runs the whole program"""
    words = hangman_helper.load_words()
    run_multiple_games(words)


if __name__ == "__main__":
    main()
