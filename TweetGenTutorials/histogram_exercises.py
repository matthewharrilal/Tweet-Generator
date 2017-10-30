import random
from functools import reduce

word_file = open("/usr/share/dict/words")
read_file = word_file.read()
split_file = read_file.split()
word_list = ["Matthew", "Corey", "Harrilal", "Corey", "Justin", "Justin", "Steven", "Rohan", "Willie", "Willie", "Elliot"]

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



def histogram(word_list):

# So essentially what this function will do is that it will take the unique words as a key in a dictionary and as a value the freu
   word_frequency = {}
   for word in word_list:
       occurences = word_list.count(word)
       word_frequency[word] = occurences
   return word_frequency


print(histogram(word_list))