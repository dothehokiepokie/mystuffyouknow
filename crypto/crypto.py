# imports random module
import random

# input word abcd is repeated twice
word = "abcdwxyz"

# string made from input word
string_made_from_input_word = ""

# single alphabet letter


def single_letter_of_alphabet():
    number_1 = random.randint(10, 35)

    if(number_1 == 10):
        return "a"
    elif(number_1 == 11):
        return "b"
    elif(number_1 == 12):
        return "c"
    elif(number_1 == 13):
        return "d"
    elif(number_1 == 14):
        return "e"
    elif(number_1 == 15):
        return "f"
    elif(number_1 == 16):
        return "g"
    elif(number_1 == 17):
        return "h"
    elif(number_1 == 18):
        return "i"
    elif(number_1 == 19):
        return "j"
    elif(number_1 == 20):
        return "k"
    elif(number_1 == 21):
        return "l"
    elif(number_1 == 22):
        return "m"
    elif(number_1 == 23):
        return "n"
    elif(number_1 == 24):
        return "o"
    elif(number_1 == 25):
        return "p"
    elif(number_1 == 26):
        return "q"
    elif(number_1 == 27):
        return "r"
    elif(number_1 == 28):
        return "s"
    elif(number_1 == 29):
        return "t"
    elif(number_1 == 30):
        return "u"
    elif(number_1 == 31):
        return "v"
    elif(number_1 == 32):
        return "w"
    elif(number_1 == 33):
        return "x"
    elif(number_1 == 34):
        return "y"
    elif(number_1 == 35):
        return "z"


# make the string for the list with the letter first, then the number key that says how to hide the letter with crypto


def make_string(word_letter, add):
    if add == "no_letter_added":
        return word_letter + "1"
    if add == "right_letter_added":
        return word_letter + "2"
    if add == "left_letter_added":
        return word_letter + "3"
    if add == "left_letter_added_right_letter_added":
        return word_letter + "4"


# the counter changes the crypto key
counter = 1

# list of letters paired with their crypto key
# putting the lists in the program together so they're easier to keep track of
list_of_letters = []
list_of_numbers = []

list_of_list_of_letters = []
list_of_list_of_numbers = []

# cycle the counter through the input
for x in range(1, 5):
    counter = x
    # loop through word making a pair of string, first element is the word letter,
    # second element is the crypto to use on the letter
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

    # 5 numbers
    # the first and second numbers are the letters real value
    # the third and fourth numbers are the letters fake value
    # the last number is the code for how to hide the letter by using other letters
    # print(list_of_letters)

    for letter in list_of_letters:
        if(letter[0] == "a"):
            list_of_numbers.append(
                "01" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "b"):
            list_of_numbers.append(
                "02" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "c"):
            list_of_numbers.append(
                "03" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "d"):
            list_of_numbers.append(
                "04" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "e"):
            list_of_numbers.append(
                "05" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "f"):
            list_of_numbers.append(
                "06" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "g"):
            list_of_numbers.append(
                "07" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "h"):
            list_of_numbers.append(
                "08" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "i"):
            list_of_numbers.append(
                "09" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "j"):
            list_of_numbers.append(
                "10" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "k"):
            list_of_numbers.append(
                "11" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "l"):
            list_of_numbers.append(
                "12" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "m"):
            list_of_numbers.append(
                "13" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "n"):
            list_of_numbers.append(
                "14" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "o"):
            list_of_numbers.append(
                "15" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "p"):
            list_of_numbers.append(
                "16" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "q"):
            list_of_numbers.append(
                "16" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "r"):
            list_of_numbers.append(
                "18" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "s"):
            list_of_numbers.append(
                "19" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "t"):
            list_of_numbers.append(
                "20" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "u"):
            list_of_numbers.append(
                "21" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "v"):
            list_of_numbers.append(
                "22" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "w"):
            list_of_numbers.append(
                "23" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "x"):
            list_of_numbers.append(
                "24" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "y"):
            list_of_numbers.append(
                "25" + str(random.randint(10, 35)) + letter[1])
        elif(letter[0] == "z"):
            list_of_numbers.append(
                "26" + str(random.randint(10, 35)) + letter[1])

    # print what the crypto key means so you can undo the crypto key revealing the actual letter
    # elements 0 and 1 are the real value 10 to 36 = 26 values 1 value for every letter in the alphabet

    # for letter in list_of_numbers:
    #    if letter[4] == "1":
    #        print(letter + " no_letter_added")
    #    elif letter[4] == "2":
    #        print(letter + " right_letter_added")
    #    elif letter[4] == "3":
    #        print(letter + " left_letter_added")
    #    elif letter[4] == "4":
    #        print(letter + " left_letter_added_right_letter_added")

    # now to write the false list element 2, 3, and the crypto code element 4 into a string
    # then i join the string to a list
    # this string is only one letter from the input word

    # then make the list into a single string which is one word
    # then i make a bunch of words that is a sentence but in crypto form
    # then i can pass the string sentence into the sarcasm program
    # to find the most sarcastic word in the string and use that

    single_letter_in_original_word = ""
    counter_2 = 0
    the_crypto_word = ""

    for letter in list_of_numbers:
        if ("1" in letter[2]) & ("0" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "a"

                single_letter_in_original_word += "a"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "a"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "a"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "a"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "a"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "a"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "a"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("1" in letter[2]) & ("1" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "b"

                single_letter_in_original_word += "b"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "b"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "b"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "b"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "b"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "b"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "b"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("1" in letter[2]) & ("2" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "c"

                single_letter_in_original_word += "c"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "c"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "c"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "c"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "c"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "c"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "c"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("1" in letter[2]) & ("3" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "d"

                single_letter_in_original_word += "d"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "d"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "d"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "d"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "d"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "d"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "d"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("1" in letter[2]) & ("4" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "e"

                single_letter_in_original_word += "e"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "e"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "e"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "e"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "e"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "e"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "e"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("1" in letter[2]) & ("5" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "f"

                single_letter_in_original_word += "f"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "f"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "f"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "f"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "f"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "f"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "f"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("1" in letter[2]) & ("6" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "g"

                single_letter_in_original_word += "g"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "g"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "g"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "g"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "g"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "g"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "g"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("1" in letter[2]) & ("7" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "h"

                single_letter_in_original_word += "h"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "h"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "h"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "h"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "h"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "h"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "h"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("1" in letter[2]) & ("8" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "i"

                single_letter_in_original_word += "i"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "i"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "i"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "i"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "i"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "i"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "i"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("1" in letter[2]) & ("9" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "j"

                single_letter_in_original_word += "j"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "j"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "j"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "j"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "j"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "j"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "j"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("0" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "k"

                single_letter_in_original_word += "k"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "k"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "k"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "k"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "k"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "k"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "k"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("1" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "l"

                single_letter_in_original_word += "l"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "l"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "l"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "l"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "l"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "l"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "l"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("2" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "m"

                single_letter_in_original_word += "m"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "m"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "m"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "m"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "m"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "m"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "m"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("3" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "n"

                single_letter_in_original_word += "n"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "n"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "n"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "n"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "n"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "n"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "n"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("4" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "o"

                single_letter_in_original_word += "o"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "o"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "o"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "o"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "o"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "o"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "o"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("5" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "p"

                single_letter_in_original_word += "p"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "p"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "p"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "p"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "p"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "p"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "p"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("6" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "q"

                single_letter_in_original_word += "q"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "q"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "q"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "q"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "q"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "q"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "q"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("7" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "r"

                single_letter_in_original_word += "r"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "r"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "r"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "r"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "r"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "r"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "r"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("8" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "s"

                single_letter_in_original_word += "s"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "s"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "s"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "s"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "s"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "s"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "s"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("2" in letter[2]) & ("9" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "t"

                single_letter_in_original_word += "t"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "t"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "t"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "t"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "t"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "t"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "t"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("3" in letter[2]) & ("0" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "u"

                single_letter_in_original_word += "u"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "u"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "u"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "u"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "u"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "u"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "u"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("3" in letter[2]) & ("1" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "v"

                single_letter_in_original_word += "v"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "v"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "v"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "v"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "v"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "v"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "v"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("3" in letter[2]) & ("2" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "w"

                single_letter_in_original_word += "w"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "w"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "w"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "w"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "w"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "w"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "w"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("3" in letter[2]) & ("3" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "x"

                single_letter_in_original_word += "x"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "x"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "x"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "x"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "x"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "x"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "x"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("3" in letter[2]) & ("4" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "y"

                single_letter_in_original_word += "y"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "y"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "y"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "y"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "y"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "y"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "y"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word
        if ("3" in letter[2]) & ("5" in letter[3]):
            if "1" in letter[4]:
                # "no_letter_added"
                the_crypto_word += "z"

                single_letter_in_original_word += "z"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "2" in letter[4]:
                # right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += "z"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += "z"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "3" in letter[4]:
                # left_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "z"

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "z"

                list_of_letters[counter_2] = single_letter_in_original_word

            elif "4" in letter[4]:
                # left_letter_added_right_letter_added
                the_crypto_letter = single_letter_of_alphabet()

                the_crypto_word += the_crypto_letter
                the_crypto_word += "z"
                the_crypto_word += the_crypto_letter

                single_letter_in_original_word += the_crypto_letter
                single_letter_in_original_word += "z"
                single_letter_in_original_word += the_crypto_letter

                list_of_letters[counter_2] = single_letter_in_original_word

        single_letter_in_original_word = ""
        counter_2 += 1

    # print(list_of_numbers)
    # print(list_of_letters)
    # print(the_crypto_word)

    # append the two lists to a master list to be able to decrypt the encrypted crypto word
    list_of_list_of_letters.append(list_of_letters)
    list_of_list_of_numbers.append(list_of_numbers)

    # empty the list so its hard to find in memory
    # i will have to make a new input string from the list of letters though
    list_of_letters = []
    list_of_numbers = []

    # make the sentence from the crypto word
    if x != 4:
        string_made_from_input_word += the_crypto_word
        string_made_from_input_word += " "
    else:
        string_made_from_input_word += the_crypto_word

# original input word
print("the original input word = " + word)
print()

# each element is a single letter from the input string
# print the decryption each element number
# the first two numbers are the actual letter,
# the second and third numbers are the false letter
# the fifth number is the pattern to make from the added false letters added to the false letter
print(list_of_list_of_numbers)
print()
# print the encryption made from the decryption key
print(list_of_list_of_letters)
print()
# the 4 strings made from the one input string which makes a sentence to feed into the sarcasm program
print(string_made_from_input_word)
print()
