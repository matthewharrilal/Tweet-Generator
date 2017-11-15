import cleanup
import pdb

class Listogram(list):
    def __init__(self, word_text):
        if word_text:
            self.word_text = word_text
            for word in self.word_text:
                self.add_count(word)

    def generate_listogram(self):
        word_occurences_dictionary = {}
        word_dictionary = {}
        base_histogram_list = []
        inner_histogram_pairs = ()
        cleaned_text = cleanup.clean_given_text(self.word_text)[:100]
        for word in cleaned_text:
            word_tuple = (word, )
            word_occurences = cleaned_text.count(word)
            word_occurences_dictionary[word] = word_occurences
            if word not in inner_histogram_pairs:
                inner_histogram_pairs = word_tuple + (word_occurences, )
                print("\"{}\" appears {} times".format(word, word_occurences))
            if inner_histogram_pairs not in base_histogram_list:
                base_histogram_list.append(inner_histogram_pairs)
        print('%s tokens, %s types' %(sum(word_occurences_dictionary.values()), len(word_occurences_dictionary)))
        return base_histogram_list

    def add_count(self):
        pass

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
