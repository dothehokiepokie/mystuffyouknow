import string

# input string
str1 = "Theres a lady whos sure all that glitters is gold And shes buying a stairway to Heaven When she gets there she knows, if the stores are all closed With a word she can get what she came for Ooh, ooh, and shes buying a stairway to Heaven Theres a sign on the wall, but she wants to be sure Cause you know sometimes words have two meanings In a tree by the brook, theres a songbird who sings Sometimes all of our thoughts are misgiven Ooh, makes me wonder Ooh, makes me wonder Theres a feeling I get when I look to the west And my spirit is crying for leaving In my thoughts I have seen rings of smoke through the trees And the voices of those who stand looking Ooh, it makes me wonder Ooh, really makes me wonder And its whispered that soon if we all call the tune Then the piper will lead us to reason And a new day will dawn for those who stand long And the forests will echo with laughter Oh-oh-oh-oh-woahhh If theres a bustle in your hedgerow, dont be alarmed, now Its just a spring clean for the May queen Yes, there are two paths you can go by, but in the long run Theres still time to change the road youre on And it makes me wonder Ohh, woah Your head is humming and it wont go, in case you dont know The pipers calling you to join him Dear lady, can you hear the wind blow? And did you know Your stairway lies on the whispering wind? And as we wind on down the road Our shadows taller than our soul There walks a lady we all know Who shines white light and wants to show How everything still turns to gold And if you listen very hard The tune will come to you at last When all are one and one is all To be a rock and not to roll And shes buying a stairway to Heaven"

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

                if number_of_letters_in_the_word == short_sorted_unique_list[-1]:
                    short_new_mix_string_short += letter_string
                elif number_of_letters_in_the_word == short_sorted_unique_list[-2]:
                    short_new_mix_string_short += letter_string
                count_2 += 1

            if (word_letter in "aeiouy") & (vowel_1 > 0) & (consonant > 0) & (count == 0):

                if number_of_letters_in_the_word == long_sorted_unique_list[-3]:
                    long_new_mix_string_long += letter_string
                elif number_of_letters_in_the_word == long_sorted_unique_list[-4]:
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
