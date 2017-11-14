
import cleanup
import pdb

class Dictogram(dict):
    def __init__(self, word_text=None):
        '''Everytime this dictogram class is instantiated word text is given'''
        if word_text:
            self.word_text = word_text
            for word in self.word_text:
                self.add_count(word)


    '''Generates a dictogram given a piece of text'''
    def generate_histogram(self):
        '''This function generates our histogram for us'''
        word_frequency = {}
        cleaned_text = cleanup.clean_given_text(self.word_text)[:100]
        for word in cleaned_text:
            word_occurences = cleaned_text.count(word)
            word_frequency[word] = word_occurences
        return word_frequency

    def add_count(self, word, count=1):
        if word not in self:
            self[word] = count
        else:
            self[word] += count


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

    # def pair_text_together(self):
    #     # Pairs a given corpus into pairs of words
    #     paired_text = {}
    #     cleaned_text = cleanup.clean_given_text(self.word_text)
    #     rarest_word = max(self.generate_histogram().values())
    #     for word in range(len(cleaned_text[:10]) - 1):
    #         paired_text[cleaned_text[word]] = {cleaned_text[word + 1]: }
    #     return paired_text

    def find_word_after_entry(self, user_word_input):
        pair_text_list = list(self.pair_text_together())
        new_word = pair_text_list.index(user_word_input) + 1
        return pair_text_list[new_word]

    def generates_all_words(self):
        word_list = []
        cleaned_text = cleanup.clean_given_text(self.word_text)[:100]
        for word in cleaned_text:
            word_list.append(word)
        return word_list


    def develop_states_and_transitions(self):
        #Finds the states and transitions when given a corpus
        word_b_list = []
        rel_probability = {}
        chain_dictionary = {}
        paired_text_list = list(self.pair_text_together())
        count = 0

        while count != (len(paired_text_list) - 1):
            for word in self.generates_all_words():
                next_word_occurence = self.generates_all_words().count(self.find_word_after_entry(word))
                current_word_occurence = self.generates_all_words().count(word)
                rel_probability = next_word_occurence / current_word_occurence
                new_word = self.generates_all_words().index(word) + 1
                new_word_value = paired_text_list[new_word]
                chain_dictionary[word] = {self.find_word_after_entry(new_word_value): rel_probability}
                count = count + 1
        return chain_dictionary

    # def markov_chain(self):
    #     markov_dictionary = {}
    #     if word not in markov_dictionary.keys():
    #         markov_dictionary[word] =


cleaned_text = cleanup.clean_given_text("robert_greene.txt")[:100]

"""This function essentially makes a dictionary where the keys are the current word while the value is a dictionary
of all the possible next words"""
def markov_chain(cleaned_text):
    print(cleaned_text)
    markov_dictionary = {}
    x = 0
    while x < len(cleaned_text) -1:
        current_word = cleaned_text[x]
        next_word = cleaned_text[x + 1]
        if current_word not in markov_dictionary.keys():
            markov_dictionary[current_word] = Dictogram() # THIS IS EQUAL TO THAT BECAUSE WE DONT HAVE TO PASS IN THE TEXT YET{}
        markov_dictionary[current_word].add_count(next_word)
        x += 1
    # print(markov_dictionary)
    return markov_dictionary

# print(markov_chain(cleaned_text))
print(markov_chain("one fish two fish red fish blue fish".split()))
# print(dictogram)