
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
        for word in cleaned_text[:10]:
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

    def pair_text_together(self):
        # Pairs a given corpus into pairs of words
        paired_text = {}
        cleaned_text = cleanup.clean_given_text(self.word_text)
        rarest_word = max(self.generate_histogram().values())
        for word in range(len(cleaned_text[:10000]) - 1):
            paired_text[cleaned_text[word]] = cleaned_text[word + 1]
        return paired_text

    def find_word_before_entry(self, user_word_input):
        pair_text_list = list(self.pair_text_together())
        new_word = pair_text_list.index(user_word_input) - 1
        return pair_text_list[new_word]



    def develop_states_and_transitions(self, user_input_word_b):
        #Finds the states and transitions when given a corpus
        word_b_list = []
        word_b_occurence_dictionary = {}
        paired_text_list = list(self.pair_text_together())
        pdb.set_trace()
        user_input_occurences = paired_text_list.count(user_input_word_b)
        rel_probability = user_input_occurences / paired_text_list.count(self.find_word_before_entry(user_input_word_b))
        return rel_probability, paired_text_list


        # return paired_text_list
        # print("The count of the transitional_word is %s" % (word_b_count))
        # word_b_occurence_dictionary[user_input_word_a] = {user_input_word_b: relative_probability}
        # return word_b_occurence_dictionary



dictogram = Dictogram("robert_greene.txt")
# print(list(dictogram.pair_text_together()))

# print(dictogram.develop_states_and_transitions('the'))

print(dictogram.develop_states_and_transitions('by'))



