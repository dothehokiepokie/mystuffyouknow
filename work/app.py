import string

# input string
str1 = "The Lord word says way too bee"

# convert string to lowercase
str1 = str1.lower()

# remove punctuation from string
table = str.maketrans(dict.fromkeys(string.punctuation))
new_string = str1.translate(table)
new_string += " ."

letter_string = ""
vowel_1 = 0
consonant = 0
count = 0
count_2 = 0
new_short_string = ""
new_long_string = ""

char_count_short = []
char_count_long = []

for letter in new_string:
    letter_string += letter
    if " " in letter:
        number_of_letters_in_the_word = len(letter_string) - 1

        for word_letter in letter_string:
            if (word_letter in "aeiouy") & (vowel_1 > 1) & (consonant > 1) & (count_2 == 0):
                char_count_short.append(number_of_letters_in_the_word)
                new_short_string += letter_string
                count_2 += 1

            if (word_letter in "aeiouy") & (vowel_1 > 0) & (consonant > 0) & (count == 0):
                char_count_long.append(number_of_letters_in_the_word)
                new_long_string += letter_string
                count += 1
            if (word_letter in "bcdfghjklmnpqrstvwxz"):
                consonant += 1
            if (word_letter in "aeiouy"):
                vowel_1 += 1

        vowel_1 = 0
        consonant = 0
        count = 0
        count_2 = 0
        letter_string = ""

short_unique_set = set(char_count_short)
short_unique_list = list(short_unique_set)
short_sorted_unique_list = sorted(short_unique_list, reverse=True)

long_unique_set = set(char_count_long)
long_unique_list = list(long_unique_set)
long_sorted_unique_list = sorted(long_unique_list, reverse=True)

long_new_mix_string_long = ""
short_new_mix_string_short = ""

for letter in new_string:
    letter_string += letter
    if " " in letter:
        number_of_letters_in_the_word = len(letter_string) - 1

        for word_letter in letter_string:
            if (word_letter in "aeiouy") & (vowel_1 > 1) & (consonant > 1) & (count_2 == 0):
                if len(short_sorted_unique_list) >= 2:
                    if number_of_letters_in_the_word == short_sorted_unique_list[-1]:
                        short_new_mix_string_short += letter_string
                    elif number_of_letters_in_the_word == short_sorted_unique_list[-2]:
                        short_new_mix_string_short += letter_string
                count_2 += 1

            if (word_letter in "aeiouy") & (vowel_1 > 0) & (consonant > 0) & (count == 0):

                if len(long_sorted_unique_list) >= 4:
                    if number_of_letters_in_the_word == long_sorted_unique_list[-3]:
                        long_new_mix_string_long += letter_string
                    elif number_of_letters_in_the_word == long_sorted_unique_list[-4]:
                        long_new_mix_string_long += letter_string
                elif len(long_sorted_unique_list) >= 3:
                    if number_of_letters_in_the_word == long_sorted_unique_list[-2]:
                        long_new_mix_string_long += letter_string
                    elif number_of_letters_in_the_word == long_sorted_unique_list[-3]:
                        long_new_mix_string_long += letter_string
                elif len(long_sorted_unique_list) >= 2:
                    if number_of_letters_in_the_word == long_sorted_unique_list[-1]:
                        long_new_mix_string_long += letter_string
                    elif number_of_letters_in_the_word == long_sorted_unique_list[-2]:
                        long_new_mix_string_long += letter_string
                count += 1
            if (word_letter in "bcdfghjklmnpqrstvwxz"):
                consonant += 1
            if (word_letter in "aeiouy"):
                vowel_1 += 1

        vowel_1 = 0
        consonant = 0
        count = 0
        count_2 = 0
        letter_string = ""


print(new_long_string)
print("_________")
print(long_new_mix_string_long)
print("_________")
print(new_short_string)
print("_________")
print(short_new_mix_string_short)
