import random
from functools import reduce

word_file = open("/usr/share/dict/words")
read_file = word_file.read()
split_file = read_file.split()
word_list = ["Matthew", "Corey", "Harrilal", "Corey", "Justin", "Justin", "Steven", "Rohan", "Willie"]

# users_input = str(input())
# users_input = "Corey"
def find_frequency_of_words(users_input, word_list):
   word_frequency = {}
   # So essentially we want a key value pair where the key represents the unique wor
   if users_input in word_list:
       for _ in word_list:
           occurences = word_list.count(users_input)
           word_frequency[users_input] = occurences
   return word_frequency


def find_unique_words(word_list):
    unique_word = []
    for word in word_list:
        occurences = word_list.count(word)
        if occurences == 1:
            unique_word.append(word)
    return len(unique_word)



print(find_unique_words(word_list))

