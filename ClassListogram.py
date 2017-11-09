import cleanup
import pdb

class Listogram(list):
    def __init__(self, word_text):
        self.word_text = word_text

    def generate_listogram(self):
        base_histogram_list = []
        inner_histogram_pairs = []
        cleaned_text = cleanup.clean_given_text(self.word_text)[:100]
        for word in cleaned_text:
            word_occurences = cleaned_text.count(word)
            if word not in inner_histogram_pairs:
                inner_histogram_pairs = [word, word_occurences]
                print("\"{}\" appears {} times".format(word, word_occurences))
            if inner_histogram_pairs not in base_histogram_list:
                base_histogram_list.append(inner_histogram_pairs)
        return base_histogram_list

    def generate_specific_frequency(self):
        specific_word_pair_list = []
        user_inputted_word = str(input())
        cleaned_text = cleanup.clean_given_text(self.word_text)
        if user_inputted_word in cleaned_text:
            specific_word_occurence = cleaned_text.count(user_inputted_word)
            specific_word_pair_list = [user_inputted_word, specific_word_occurence]
        else:
            return 'The word you are searching for has a frequency of 0'
        return specific_word_pair_list

    def generate_boolean_value(self):
        in_there = True
        not_there = False
        user_inputted_word = str(input())
        for word in self.generate_listogram():
           if user_inputted_word in word:
               print("The word is in there")

        return




listogram = Listogram("robert_greene.txt")
print(listogram.generate_listogram())
