import string


def Convert(string):
    li = list(string.split(" "))
    return li


# input string
str1 = "This you have to understand. Theres only one way to hurt a man whos lost everything. Give him back something broken."

# convert string to lowercase
str1 = str1.lower()

# remove punctuation from string
table = str.maketrans(dict.fromkeys(string.punctuation))
new_string = str1.translate(table)
new_string += " ."
a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
y = "y"

letter_string = ""
vowel_1 = 0
consonant = 0
count = 0
count_2 = 0
new_short_string = ""
new_long_string = ""
for letter in new_string:
    letter_string += letter
    if " " in letter:
        for word_letter in letter_string:
            if (word_letter in "aeiouy") & (vowel_1 > 1) & (consonant > 1) & (count_2 == 0):

                new_long_string += letter_string
                count_2 += 1

            if (word_letter in "aeiouy") & (vowel_1 > 0) & (consonant > 0) & (count == 0):

                new_short_string += letter_string
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

print(new_short_string)
print("_________")
print(new_long_string)
