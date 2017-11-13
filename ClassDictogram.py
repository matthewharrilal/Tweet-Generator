
import cleanup
import pdb

class Dictogram(dict):
    def __init__(self, word_text):
        '''Everytime this dictogram class is instantiated word text is given'''
        self.word_text = word_text


    '''Generates a dictogram given a piece of text'''
    def generate_histogram(self):
        '''This function generates our histogram for us'''
        word_frequency = {}
        cleaned_text = cleanup.clean_given_text(self.word_text)[:100]
        for word in cleaned_text:
            word_occurences = cleaned_text.count(word)
            word_frequency[word] = word_occurences
        return word_frequency


    def generate_histogram_weights(self):
        #This function essentially generates the weights or the relative occurence of the words in the histogram
        weight_dictionary = {}
        sum_values = sum(self.generate_histogram().values())
        cleaned_text = cleanup.clean_given_text(self.word_text)
        for word in cleaned_text[:100]:
            word_occurences = cleaned_text.count(word)
            weighted_occurences = word_occurences / sum_values
            weight_dictionary[word] = weighted_occurences
        return weight_dictionary

    def generate_specific_frequency_of_word(self, user_inputted_word):
        # This function essentially takes a word that the user wants to find in the text and find how many times that word
        # occurs
        specific_word_frequency = {}
        user_inputted_word = str(input())
        cleaned_text = cleanup.clean_given_text(self.word_text)
        if user_inputted_word in cleaned_text:
            specific_word_occurence = cleaned_text.count(user_inputted_word)
            specific_word_frequency[user_inputted_word] = specific_word_occurence
        else:
            return 'This word does not occur at all'
        return specific_word_frequency

    def find_rarest_word(self):
        rarest_word = {}
        highest_occurence = max(self.generate_histogram().values())
        for key, value in self.generate_histogram().items():
            if value == highest_occurence:
                rarest_word[key] = value
        return rarest_word

    word_list = ["Matthew", "Ralph", "Harrilal", "Ralph", "Ralph", "Tyler", "Matthew"]

    def develop_states_and_transitions(self):
        #Finds the states and transitions when given a corpus
        paired_text = {}
        word_a_list = []
        rel_probability_dictionary = {}
        cleaned_text = cleanup.clean_given_text(self.word_text)
        rarest_word = max(self.generate_histogram().values())
        for word in range(len(cleaned_text[:10]) - 1):
            paired_text[cleaned_text[word]] = cleaned_text[word + 1]
        sum_values = len(paired_text.values())
        print('These are the sum_values %s' %(sum_values))
        for word_a in paired_text.keys():
            word_a_list.append(word_a)
        for word in word_a_list:
            word_a_occurences = word_a_list.count(word)
            relative_probability = word_a_occurences / sum_values
            rel_probability_dictionary[word] = relative_probability

        return rel_probability_dictionary






dictogram = Dictogram("robert_greene.txt")


print(dictogram.develop_states_and_transitions())

