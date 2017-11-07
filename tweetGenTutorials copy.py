import random
from itertools import permutations
import time

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!",
          "Matthew is simply awesome")


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]


def randomize_given_words(text):
    split_text = text.split(" ")
    print(split_text)
    rand_index = random.randint(0, len(split_text) - 1)
    return split_text[rand_index]


# The purpose of the next two functions is to either reverse the given word or the given sentence
def word_and_sentence_reversal(text):
    #Since we are reversing the given word we can reverse them using the indexes
    reversed_text = text[::-1]
    return reversed_text


word_file = open("/usr/share/dict/words")
read_file = word_file.read()
split_file = read_file.split()


def permutations_method(word):
    perms = [''.join(p) for p in permutations(word)]
    return perms

def anagram_generator(split_file):
    random_index = random.randint(0, len(split_file) - 1)
    random_word = split_file[random_index]
    random_word_length = len(random_word)
    same_length_words = list(filter(lambda x: len(x) == random_word_length, split_file))
    # for word in permutations_method(random_word):
    #     print(word)
    combos = permutations_method(random_word)
    # for word in combos:
    #     if word in same_length_words:
    #         print(random_word)
    #         return(''.join(set(word)))
    deleted_duplicate_combos = (list(set(combos)))
    for word in deleted_duplicate_combos:
        if word in same_length_words:
            print(random_word)
            return ''.join(set(word))
    return ''

def see_if_word_accurate(word):
    if word in split_file:
        print('the word is in the file')
    else:
        print("the word is not in the split file")


def autocomplete_word(split_file):
    random_index = random.randint(0, len(split_file) - 1)
    random_word = split_file[random_index]
    abbreviated_word = random_word[:3]
    print("The abbreviated word is %s" %(abbreviated_word))
    for word in split_file:
        if abbreviated_word == word[:3]:
            print(word)
    return ''

if __name__ == '__main__':
    print(anagram_generator(split_file))