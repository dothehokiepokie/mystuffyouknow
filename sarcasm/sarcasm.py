import string

# Python3 program to Split string into characters


def split(word):
    return {char for char in word}

# pass list into function


def printing_magicians(word):
    first_word_letters = ""
    second_word_letters = ""

    if(len(word) % 2):
        first_half = word[:len(word) // 2 + 1]
        second_half = word[len(word) // 2:]

        for letter in first_half:
            first_word_letters += letter

        for letter in second_half:
            second_word_letters += letter

    else:
        first_half = word[:len(word) // 2]
        second_half = word[len(word) // 2:]

        for letter in first_half:
            first_word_letters += letter

        for letter in second_half:
            second_word_letters += letter

    return first_word_letters, second_word_letters

# Python code to convert string to list


def Convert(string):
    li = list(string.split(" "))
    return li


# input string
str1 = "That's just what I needed today!"
# convert string to lowercase
str1 = str1.lower()

# remove punctuation from string
table = str.maketrans(dict.fromkeys(string.punctuation))
new_s = str1.translate(table)


list_of_words = Convert(new_s)  # convert string to list

first_word_letters = ""
second_word_letters = ""

# sort sentence words to half the word
# then join the half of the word from each word in the sentence
# to a single first half or second half word
for x in range(len(list_of_words)):
    first_half, second_half = printing_magicians(list_of_words[x])
    first_word_letters += first_half
    second_word_letters += second_half

# remove duplicate letters from first half and second half word strings
unique_first_half_letters = "".join(set(first_word_letters))
unique_second_half_letters = "".join(set(second_word_letters))

# make half word strings into a two sets, so i can find the overlapping letters in the next step
list_of_unique_first_half_letters = split(unique_first_half_letters)
list_of_unique_second_half_letters = split(unique_second_half_letters)

# the set thats the overlapping letters from the first half and second half word strings
overlapping_letters = list_of_unique_first_half_letters & list_of_unique_second_half_letters

# convert the type set to type string
# so i can find the word with the most matching characters in the next step
string_of_overlapping_letters = str(overlapping_letters)

print("these are the overlapping sarcastic letters: " +
      string_of_overlapping_letters)


a_set = {}
e_set = {}
i_set = {}
o_set = {}
u_set = {}
y_set = {}
char_frequency = {}
# finding the word in the string with the most matching letters
# first i pass the single word into the for loop
for y in range(len(list_of_words)):
    count = 0
    for x in string_of_overlapping_letters:
        if(x.isalnum()):
            if(x in list_of_words[y]):
                # print(x)
                count += 1
    string_count = str(count)
    if "a" in list_of_words[y]:
        if list_of_words[y] not in a_set:
            a_set[list_of_words[y]] = string_count
    if "e" in list_of_words[y]:
        if list_of_words[y] not in e_set:
            e_set[list_of_words[y]] = string_count
    if "i" in list_of_words[y]:
        if list_of_words[y] not in i_set:
            i_set[list_of_words[y]] = string_count
    if "o" in list_of_words[y]:
        if list_of_words[y] not in o_set:
            o_set[list_of_words[y]] = string_count
    if "u" in list_of_words[y]:
        if list_of_words[y] not in u_set:
            u_set[list_of_words[y]] = string_count
    if "" in list_of_words[y]:
        if list_of_words[y] not in y_set:
            y_set[list_of_words[y]] = string_count
    # print(
    #    "\"" + list_of_words[y] + "\"" + " has this many matching sarcastic letter " + string_count)

a_list = list(sorted(a_set.items(), key=lambda kv: kv[1]))

e_list = list(sorted(e_set.items(), key=lambda kv: kv[1]))

i_list = list(sorted(i_set.items(), key=lambda kv: kv[1]))

o_list = list(sorted(o_set.items(), key=lambda kv: kv[1]))

u_list = list(sorted(u_set.items(), key=lambda kv: kv[1]))

y_list = list(sorted(y_set.items(), key=lambda kv: kv[1]))

aeiouy_list = a_list + e_list + i_list + o_list + u_list + y_list
thin_list = []
count = 0
for value in aeiouy_list:
    for value_2 in thin_list:
        if value[0] == value_2[0]:
            count = 1
    if count == 0:
        thin_list.append(value)
    count = 0
string_1 = ""
string_2 = ""
string_3 = ""
string_4 = ""
final_string = ""

count_word_one = 0
count_word_two = 0
count_word_three = 0
count_word_four = 0
len_word_one = 0
len_word_two = 0
len_word_three = 0
len_word_four = 0

for value in thin_list:
    if count_word_one == 0:
        count_word_one = 1
        if value[1] != "0":
            string_1 += " "
            string_1 += value[0]
            string_1 += " "
            string_1 += value[1]
            string_1 += "\n"
        len_word_one = len(value[0])

        if value == thin_list[-1]:
            final_string += value[0]

    elif count_word_two == 0:
        count_word_two = 1
        if value[1] != "0":
            string_2 += " "
            string_2 += value[0]
            string_2 += " "
            string_2 += value[1]
            string_2 += "\n"
        len_word_two = len(value[0])

        if value == thin_list[-1]:
            if len_word_one > len_word_two:
                string_1 += string_2
                final_string += string_1
            else:
                string_2 += string_1
                final_string += string_2

    elif count_word_three == 0:
        count_word_three = 1
        if value[1] != "0":
            string_3 += " "
            string_3 += value[0]
            string_3 += " "
            string_3 += value[1]
            string_3 += "\n"
        len_word_three = len(value[0])

        if value == thin_list[-1]:
            if len_word_one > len_word_two:
                string_1 += string_2
                string_1 += string_3
                final_string += string_1
            else:
                string_2 += string_1
                string_2 += string_3
                final_string += string_2

    elif count_word_four == 0:
        count_word_four = 1
        if value[1] != "0":
            string_4 += " "
            string_4 += value[0]
            string_4 += " "
            string_4 += value[1]
            string_4 += "\n"
        len_word_four = len(value[0])

        if len_word_one > len_word_two:
            string_1 += string_2
            if len_word_three > len_word_four:
                string_4 += string_3
                string_1 += string_4
                final_string += string_1
                count_word_one = 0
                count_word_two = 0
                count_word_three = 0
                count_word_four = 0
                len_word_one = 0
                len_word_two = 0
                len_word_three = 0
                len_word_four = 0
                string_1 = ""
                string_2 = ""
                string_3 = ""
                string_4 = ""
            else:
                string_3 += string_4
                string_1 += string_3
                final_string += string_1
                count_word_one = 0
                count_word_two = 0
                count_word_three = 0
                count_word_four = 0
                len_word_one = 0
                len_word_two = 0
                len_word_three = 0
                len_word_four = 0
                string_1 = ""
                string_2 = ""
                string_3 = ""
                string_4 = ""
        else:
            string_2 += string_1
            if len_word_three > len_word_four:
                string_4 += string_3
                string_2 += string_4
                final_string += string_2
                count_word_one = 0
                count_word_two = 0
                count_word_three = 0
                count_word_four = 0
                len_word_one = 0
                len_word_two = 0
                len_word_three = 0
                len_word_four = 0
                string_1 = ""
                string_2 = ""
                string_3 = ""
                string_4 = ""
            else:
                string_3 += string_4
                string_2 += string_3
                final_string += string_2
                count_word_one = 0
                count_word_two = 0
                count_word_three = 0
                count_word_four = 0
                len_word_one = 0
                len_word_two = 0
                len_word_three = 0
                len_word_four = 0
                string_1 = ""
                string_2 = ""
                string_3 = ""
                string_4 = ""
print(final_string)
