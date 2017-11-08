
import cleanup
import pdb

class Dictogram(dict):
    # def __init__(self, word_text):
    #     '''Everytime this dictogram class is instantiated word text is given'''
    #     word_text = word_text
    #

'''Generates a dictogram given a piece of text'''
    def generate_histogram(self, word_text):
        '''This function generates our histogram for us'''
        word_frequency = {}
        cleaned_text = cleanup.clean_given_text("robert_greene.txt")[:1000]
        for word in cleaned_text:
            word_occurences = cleaned_text.count(word)
            word_frequency[word] = word_occurences
        return word_frequency


dictogram = Dictogram()
print(dictogram.generate_histogram("robert_greene.txt"))