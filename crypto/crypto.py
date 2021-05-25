# imports random module
import random

# make the string for the list with the letter first then the key thats crypto obfuscation of additional letters


def make_string(word_letter, add):
    if add == "no_letter_added":
        return word_letter + "1"
    if add == "right_letter_added":
        return word_letter + "2"
    if add == "left_letter_added":
        return word_letter + "3"
    if add == "left_letter_added_right_letter_added":
        return word_letter + "4"


# word abcd is repeated twice
word = "abcde"

# the counter changes the crypto key
counter = 1

# list of letters paired with their crypto key
list_of_letters = []

# cycle the counter through the input
for x in range(1, 5):
    counter = x
    # loop through word making a pair of 2 cryptokey numbers for the one the word, time sensitive which pair to use
    for letter in word:
        if counter == 1:
            letter = make_string(letter, "no_letter_added")
            counter = 2
            list_of_letters += [letter]

        elif counter == 2:
            letter = make_string(letter, "right_letter_added")
            counter = 3
            list_of_letters += [letter]

        elif counter == 3:
            letter = make_string(letter, "left_letter_added")
            counter = 4
            list_of_letters += [letter]

        elif counter == 4:
            letter = make_string(
                letter, "left_letter_added_right_letter_added")
            if word[0] == letter:
                counter = 1
            else:
                counter = 2
            list_of_letters += [letter]

    # print the list of letters and their crypto keys
    print(list_of_letters)

    # print what the crypto key means so you can undo the crypto key revealing the actual letter
    for letter in list_of_letters:
        if "1" in letter:
            print(letter[0] + " no_letter_added")
        elif "2" in letter:
            print(letter[0] + " right_letter_added")
        elif "3" in letter:
            print(letter[0] + " left_letter_added")
        elif "4" in letter:
            print(letter[0] + " left_letter_added_right_letter_added")

    # empty the list so its hard to find in memory
    list_of_letters = []
