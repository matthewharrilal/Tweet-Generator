import random
from functools import reduce

word_file = open("/usr/share/dict/words")
read_file = word_file.read()
split_file = read_file.split()
word_list = ["Matthew", "Corey", "Harrilal", "Corey", "Justin", "Justin", "Steven"]

users_input = str(input())
# users_input = "Corey"
def find_frequency_of_words(users_input, word_list):
   word_frequency = {}
   # So essentially we want a key value pair where the key represents the unique wor
   if users_input in word_list:
       for _ in word_list:
           occurences = word_list.count(users_input)
           word_frequency[users_input] = occurences
   return word_frequency



print(find_frequency_of_words(users_input, word_list))
