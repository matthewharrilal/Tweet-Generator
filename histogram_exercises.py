import creating_randomness
import pdb
import random

word_file = open("robert_greene.txt")
read_file = word_file.read()
split_file = read_file.split()

# Instead of hardcoding the text file you want to open you can pass it as an argument therefore it can be dynamic
word_list = ["Matthew", "Ralph", "Harrilal", "Ralph", "Ralph", "Tyler", "Matthew"]


# users_input = str(input())
# users_input = "Corey"
def find_frequency_of_words(users_input, word_list):
   #  This function essentially finds the frequency of the word that the user wants to input
   word_frequency = {}
   # So essentially we want a key value pair where the key represents the unique wor
   if users_input in word_list:
       for _ in word_list:
           occurences = word_list.count(users_input)
           print(occurences)
           word_frequency[users_input] = occurences
   return word_frequency


def find_unique_words(word_list):
    # This function essentially finds all the unique words given a text
    unique_word = []
    for word in word_list:
        occurences = word_list.count(word)
        if occurences == 1:
            unique_word.append(word)
    return "The unique words are %s" %(unique_word)


# GLOBAL!!!!!
word_frequency = {}
def histogram(word_list):
   #  This function essentially formulates the histogram
   for word in word_list:
       occurences = word_list.count(word)
       print(occurences)
       word_frequency[word] = occurences
   return word_frequency


def generate_weights(word_list):
    # This function essentially generates the weights or the relative frequency of the elements passed in as the text
    weight_dictionary = {}
    sum_values = sum(histogram(word_list).values())
    for word in word_list:
        word_occurences = word_list.count(word)
        weighted_occurences = word_occurences / sum_values
        weight_dictionary[word] = weighted_occurences
    return weight_dictionary



def list_of_tuples_histogram(word_list):
    #So essentially what this function will consist of is making the histogram into a list of tuples
    base_list = []
    structured_tuple = ()

    for word in word_list:
        word_tuple = (word, )
        occurences = word_list.count(word)
        word_occurences = occurences
        if word not in structured_tuple:
            structured_tuple = word_tuple + (word_occurences, )
        if structured_tuple not in base_list:
            base_list.append(structured_tuple)

    return base_list

def generate_histogram_weights_with_tuple(word_list):
    base_list = []
    structured_tuple = ()
    sum_values = sum(list_of_tuples_histogram(word_list))

    for word in word_list:
        weighted_occurences = word_list.count(word) / sum_values
        word_tuple = (word, )
        if word not in structured_tuple:
            structured_tuple = word_tuple + (weighted_occurences, )
        if structured_tuple not in base_list:
            base_list.append(structured_tuple)
    return base_list

def list_of_lists_histogram(word_list):
    base_list = []
    structured_list = []
    for word in word_list:
        occurences = word_list.count(word)
        if word not in structured_list:
            structured_list = [word,occurences]
        if structured_list not in base_list:
            base_list.append(structured_list)
    second_element = [x[1] for x in base_list]
    return second_element

def generate_histogram_weight_with_list_of_lists(word_list):
    base_list = []
    structured_list = []
    sum_values = sum(list_of_tuples_histogram(word_list))
    for word in word_list:
        weighted_occurences = word_list.count(word) / sum_values
        if word not in structured_list:
            structured_list = [word, weighted_occurences]
        if structured_list not in base_list:
            base_list.append(structured_list)
    return base_list


def generate_random_histogram_word():
    # This function essentially generates a random word from the histogram
    for word in word_list:
        # random_word = creating_randomness.gen_random_range(word_list[0], [])
        random_index = creating_randomness.gen_random_range(0, len(word_list) -1)
        random_word = word_list[random_index]
    return random_word

#
# def time_random():
#     return(time() - float(str(time()).split('.')[0]))
#
# def gen_random_range(min, max):
#     return int(time_random() * (max + min) - min)


def generate_random_relative_word(word_list, probabilities):
    randomly_generated_number = creating_randomness.gen_random_range(0, 1)
    cumalitive_probability = 0.0
    for word, weighted_occurence in zip(word_list, probabilities):
        cumalitive_probability += weighted_occurence
        if randomly_generated_number < cumalitive_probability:
            break
    return word

print(generate_weights(word_list))