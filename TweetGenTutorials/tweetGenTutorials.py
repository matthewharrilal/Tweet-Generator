import random
from itertools import permutations

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!",
          "Matthew is simply awesome")


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]


def randomize_given_words(text):
    split_text = list(text.split(" "))
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
    for words_in_split_file in split_file:
        if random_word_length == len(words_in_split_file):
           for combination in permutations_method(random_word):
               if any(combination) == words_in_split_file:
                   print(combination)


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
   print(permutations_method("google"))