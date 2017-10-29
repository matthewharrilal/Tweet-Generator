import random
from functools import reduce

word_file = open("/usr/share/dict/words")
read_file = word_file.read()
split_file = read_file.split()
word_list = ["Matthew", "Corey", "Harrilal", "Corey", "Justin", "Justin", "Steven"]

def find_frequency_of_words(split_file):
   word_frequency = {}
   # So essentially we want a key value pair where the key represents the unique wor
   for word in split_file:
       occurences = split_file.count(word)
       word_frequency[word] = occurences
       # if occurences == 1:
       #     word_frequency[word] = occurences
   return word_frequency



print(find_frequency_of_words(word_list))