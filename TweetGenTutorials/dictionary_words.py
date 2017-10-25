import random

word_file = open("/usr/share/dict/words")
read_file = word_file.read()
split_file = read_file.split()
print(split_file)
# So the goal is to now take this list and somehow provide a way to generate random grouping of these words

def random_sentence(split_file):
    sentence_array = []
    for _ in range(11):
        random_index = random.randint(0, len(split_file) - 1)
        sentence_array.append(split_file[random_index])
    return sentence_array


    random_index = random.randint(0, len(split_file) -1)
    # sentence_array.append(split_file[random_index])
    # return sentence_array
sentence = random_sentence(split_file)
string_sentence = ' '.join(sentence)
print(string_sentence)

