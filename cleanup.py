


def clean_given_text(word_text):
    word_file = open(word_text)
    read_file = word_file.read()
    split_file = read_file.split()
    return split_file

