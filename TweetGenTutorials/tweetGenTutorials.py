import random

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

# def anagram_generator(split_file):
#     random_index = random.randint(0, len(split_file) - 1)
#     random_word = split_file[random_index]
#     listed_word = list(random_word)
#     shuffled_word = random.shuffle(listed_word)
#     new_word = ''.join(listed_word)
#     return(random_word,new_word)

def anagram_generator(split_file):
    random_index = random.randint(0, len(split_file) - 1)
    random_word = split_file[random_index]
    # return len(random_word)
    for word in split_file:
       if len(word) == len(random_word):
          print(list(word))

if __name__ == '__main__':
    quote = anagram_generator(split_file)
    print(quote)
    # print(split_file)