import creating_randomness
import pdb
import random

word_file = open("/usr/share/dict/words")
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



def list_of_tuples_histogram():
    # This function essentially displays the histogram as a tuple rather than a dictionary
    list_of_tuples = list((zip(histogram(word_list).keys(), histogram(word_list).values())))
    return list_of_tuples

def generate_histogram_weight_with_tuples(word_list):
    #First things first what we have to do is instantiate an empty tuple
    weight_tuple = ()
    # We also have to find the sum of all the frequencies therefore we can find the frequency and use this to calculate into the weighted frequency
    sum_of_frequencies = sum(histogram(word_list).values())

    #Secondly we now have to gain access to the words or the elements in the array
    for word in word_list:
        #Once we get the words we then have to find the count for the word
        word_occurence = word_list.count(word)
        weight_occurence = word_occurence / sum_of_frequencies
    #     weight_tuple = weight_tuple + (word , weight_occurence)
        if word not in weight_tuple:
            weight_tuple = weight_tuple + (word, weight_occurence)
    return weight_tuple
    # return weight_tuple

def list_of_lists_histogram():
    #This function essentially displays the histogram as a list of lists rather than a dictionary
    base_list = []
    for key, value in histogram(word_list).items():
        structured_list = [key, value]
        base_list.append(structured_list)
    return base_list

def generate_histogram_weight_with_list_lists(word_list):
    base_list = []
    key_and_weight_list = []
    sum_of_frequencies = (sum(histogram(word_list).values()))
    for key,value in histogram(word_list).items():
        word_occurence = word_list.count(key)
        weighted_occurence = word_occurence / sum_of_frequencies
        if key not in key_and_weight_list:
            key_and_weight_list = [key, weighted_occurence]
            base_list.append(key_and_weight_list)
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


def generate_random_relative_word(word_list):
    base_dictionary = {}
    relative_probability = generate_weights(word_list)
    # percent_probability = relative_probability * 100
    for key, value in relative_probability.items():
        percent_probability = value * 100
        if value not in base_dictionary:
            # base_list.append(percent_probability)
            base_dictionary[key] = percent_probability
    return base_dictionary









def while_loops():
    matthew = 0
    while matthew < 7:
        print("good")
        matthew = matthew + 1

x = creating_randomness.gen_random_range(0,1)
print(x)