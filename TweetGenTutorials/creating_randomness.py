from time import time
import math


word_list = ["Matthew", "Ralph", "Harrilal", "Ralph", "Ralph", "Tyler", "Matthew"]

def time_random():
    return(time() - float(str(time()).split('.')[0]))

def gen_random_range(min, max):
    return float(time_random() * (max + min) - min)


#
# print(generate_random_relative_word(word_list))