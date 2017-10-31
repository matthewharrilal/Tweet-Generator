from time import time
import math

def time_random():
    return(time() - float(str(time()).split('.')[0]))

def gen_random_range(min, max):
    return int(time_random() * (max + min) - min)

print(gen_random_range(0,43))