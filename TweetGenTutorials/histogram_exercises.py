def dictionary_word_frequency():
    number_dictionary = {1: 27, 34: 1, 3: 72, 4: 62, 5: 33, 6: 36, 7: 20, 8: 12, 9: 9, 10: 6, 11: 5, 12: 8, 2: 74, 14: 4, 15: 3, 16: 1, 17: 1, 18: 1, 19: 1, 21: 1, 27: 2}

    number_frequency = []

    for number in number_dictionary.values():
        number_frequency.append(list(number_dictionary.values()).count(number))
    print(list(zip(number_dictionary.keys(), number_dictionary.values())))
    return number_frequency
    # return list(zip(word_dictionary.keys(), word_dictionary.values()))

def list_of_lists_frequency():
    list_of_lists = [[7, 8, 9], [7, 8, 9], [7, 8, 9], [7, 8, 9], [7, 8, 9], [7, 8, 9], [7, 8, 9], [7, 8, 9], [7, 8, 9], [7, 8, 9]]

    list_frequency = []

    for list in list_of_lists:
        for _ in list:
            list_frequency.append(list_of_lists.count(list))
    print(list_frequency)


list_of_lists_frequency()