
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




if __name__ == '__main__':
    quote = randomize_given_words("hello the name is")
    print(q
