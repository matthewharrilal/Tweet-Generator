# import cleanup
import pdb
import string
import re
# class Listogram(list):
#     def __init__(self, word_text):
#         if word_text:
#             self.word_text = word_text
#             for word in self.word_text:
#                 self.add_count(word)
#
#     def generate_listogram(self):
#         word_occurences_dictionary = {}
#         word_dictionary = {}
#         base_histogram_list = []
#         inner_histogram_pairs = ()
#         cleaned_text = cleanup.clean_given_text(self.word_text)[:100]
#         for word in cleaned_text:
#             word_tuple = (word, )
#             word_occurences = cleaned_text.count(word)
#             word_occurences_dictionary[word] = word_occurences
#             if word not in inner_histogram_pairs:
#                 inner_histogram_pairs = word_tuple + (word_occurences, )
#                 print("\"{}\" appears {} times".format(word, word_occurences))
#             if inner_histogram_pairs not in base_histogram_list:
#                 base_histogram_list.append(inner_histogram_pairs)
#         print('%s tokens, %s types' %(sum(word_occurences_dictionary.values()), len(word_occurences_dictionary)))
#         return base_histogram_list
#
#     def add_count(self):
#         pass
#
#     def generate_specific_frequency(self):
#         specific_word_pair_list = []
#         user_inputted_word = str(input())
#         cleaned_text = cleanup.clean_given_text(self.word_text)
#         if user_inputted_word in cleaned_text:
#             specific_word_occurence = cleaned_text.count(user_inputted_word)
#             specific_word_pair_list = [user_inputted_word, specific_word_occurence]
#         else:
#             return 'The word you are searching for has a frequency of 0'
#         return specific_word_pair_list
#
#     def generate_boolean_value(self):
#         in_there = True
#         not_there = False
#         user_inputted_word = str(input())
#         for word in self.generate_listogram():
#            if user_inputted_word in word:
#                print("The word is in there")
#
#         return
#
#
# listogram = Listogram("robert_greene.txt")
#
# print(listogram.generate_listogram())







# # hexadecimal_count += (2 ** (power_position - 1) * hexdigit)
        # for key, value in hex_dict.items():
        #     if hexdigit == key:
        #         # hexadecimal_count += (2 ** (power_position - 1) ** value)
        #         print("Equals letter")
        #     else:
        #         print("Does Not")





def transform_letter_into_integer(letter):
    hex_dict = {'0': 0,'1':1,'2':2, '3': 3, '4':4, '5': 5, '6': 6, '7': 7, '8':8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P':25, 'Q': 26, 'R': 27, 'S': 28, 'T':29, 'U':30, 'V':31,'W':32, 'X': 33, 'Y':34, 'Z': 35}
    return hex_dict[letter]


def decode_hexadecimals(digits):
    hexadecimal_digit_list = list(digits.upper())
    print(hexadecimal_digit_list)

    hexadecimal_count = 0

    len_of_hexadecimal_digit_list = len(hexadecimal_digit_list)
    # pdb.set_trace()
    for index, hexdigit in enumerate(hexadecimal_digit_list):
        power_position = len_of_hexadecimal_digit_list - index

        if type(hexdigit) == str:
            hexadecimal_count += (16 ** (power_position - 1) * transform_letter_into_integer(hexdigit))
        else:
            print(type(hexdigit))
            hexadecimal_count += (16 ** (power_position - 1) * hexdigit)

    return hexadecimal_count


# print(decode('99'))


def decode_from_any_base(digit, base):
    any_base_digit_list = list(digit.upper())

    cumalitive_count = 0

    len_of_digit_list = len(any_base_digit_list)


    for index, base_digit in enumerate(any_base_digit_list):
        power_position = len_of_digit_list - index
        digit_value = transform_letter_into_integer(base_digit)
        if digit_value < base:
            exponent = power_position - 1
            cumalitive_count += (base ** exponent * digit_value)
        else:
            raise ValueError('base is out of range: {}'.format(base))

    return cumalitive_count

def transform_letter():
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',  15: 'F'}
    # hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
    #             'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22,
    #             'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
    #             'Y': 34, 'Z': 35}
    return hex_dict


def encode_from_base_ten_to_any_base(digits, base):
    remainder_list = []
    remainder = digits % base

    if digits < base and base <= 10 :
        return "Any digit lower than base is the digit itself:  %s" %(digits)

    if digits in transform_letter():
        #todo Giving me problems when given the problem to encode 10 to base 10
        return transform_letter()[digits]

    while digits >= base:

        digits //= base
        remainders = digits % base
        remainder_list.append(remainders)
        reversed_remainder_list = remainder_list[::-1]
        reversed_remainder_list.remove(reversed_remainder_list[0])
        reversed_remainder_list.append(remainder)
    prepended_reversed_remainder_list = [digits] + reversed_remainder_list
    # return ''.join(str(x) for x in prepended_reversed_remainder_list)
    return prepended_reversed_remainder_list


def encode_base_ten_to_hexadecimal(list_of_digits):
    newer_list = []
    for index,digit in enumerate(list_of_digits):
        if digit in transform_letter().keys():
            list_of_digits[index] = transform_letter()[digit]
    pretty_printed_result = ''.join(str(number) for number in list_of_digits)
    return pretty_printed_result.lower()

#
# # print(encode_base_ten_to_hexadecimal(encode_from_base_ten_to_any_base(4027038225, 16)))
# print(transform_letter(10))
print(encode_base_ten_to_hexadecimal(encode_from_base_ten_to_any_base(1,2)))


def find_remainder(digits, base):
    return digits % base


# TESTS THAT DO NOT WORK assert encode(1234, 32) == '16i',assert encode(10, 2) == '1010',assert encode(10, 10) == '10', assert encode(248975, 16) == '3cc8f'
#         assert encode(248975, 25) == 'fn90'
#         assert encode(248975, 32) == '7j4f'
#         assert encode(248975, 36) == '5c3z'
# assert encode(1234, 32) == '16i'
# assert encode(10, 10) == '10'
# assert encode(10, 2) == '1010'    MOST OF THESE TO FIX YOU JUST HAVE TO FIX THE CONDITION CHECKING IF THE DIGIT IS IN THE DICTIONARY
#         assert encode(11, 2) == '1011'
#         assert encode(12, 2) == '1100'
#         assert encode(13, 2) == '1101'
#         assert encode(14, 2) == '1110'
#         assert encode(15, 2) == '1111'