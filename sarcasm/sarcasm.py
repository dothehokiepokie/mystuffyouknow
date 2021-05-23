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
str1 = "revenge is a dish best served cold"
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

# finding the word in the string with the most matching letters
# first i pass the single word into the for loop
for y in range(len(list_of_words)):
    count = 0
    for x in string_of_overlapping_letters:
        if(x.isalnum()):
            if(x in list_of_words[y]):
                print(x)
                count += 1
    string_count = str(count)
    print(
        "\"" + list_of_words[y] + "\"" + " has this many matching sarcastic letter " + string_count)
