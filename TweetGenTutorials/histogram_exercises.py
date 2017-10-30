import random
from functools import reduce

word_file = open("/usr/share/dict/words")
read_file = word_file.read()
split_file = read_file.split()
word_list = ["Matthew", "Corey", "Harrilal", "Corey", "Corey"]

# users_input = str(input())
# users_input = "Corey"
def find_frequency_of_words(users_input, word_list):
   word_frequency = {}
   # So essentially we want a key value pair where the key represents the unique wor
   if users_input in word_list:
       for _ in word_list:
           occurences = word_list.count(users_input)
           print(occurences)
           word_frequency[users_input] = occurences
   return word_frequency


def find_unique_words(word_list):
    unique_word = []
    for word in word_list:
        occurences = word_list.count(word)
        if occurences == 1:
            unique_word.append(word)
    return "The unique words are %s" %(unique_word)


word_frequency = {}
def histogram(word_list):

# So essentially what this function will do is that it will take the unique words as a key in a dictionary and as a value the freu

   for word in word_list:
       occurences = word_list.count(word)
       print(occurences)
       word_frequency[word] = occurences
   return word_frequency


def generate_random_histogram_word():
    user_input = str(input()).split()
    for word in histogram(user_input):
        random_index = random.randint(0 , len(user_input) - 1)
        random_word = user_input[random_index]
    return random_word


def generate_weights(word_list):
    weight_dictionary = {}
    sum_values = sum(histogram(word_list).values())
    for word in word_list:
        word_occurences = word_list.count(word)
        weighted_occurences = word_occurences / sum_values
        weight_dictionary[word] = weighted_occurences
    return weight_dictionary


def list_of_tuples_histogram(word_list):
    list_of_lists = list((zip(histogram(word_list).keys(), histogram(word_list).values())))
    return list_of_lists

print(list_of_tuples_histogram(word_list))
