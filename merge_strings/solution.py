import math


def merge_strings(string_1, string_2):
    """
    Function to merge two strings together.
    e.g: '1111' + '000000' gives '1010101000'
    :param string_1: A first string
    e.g: '1111'
    :param string_2: Another string
    e.g: '000000'
    :return:
    """
    last_index = 0
    final_string = ''
    largest_string = string_2 if len(string_2)>len(string_1) else string_1
    values_range = 2 * min(len(string_1), len(string_2))
    for element in range(values_range):
        if element % 2 == 0 or element == 0:
            final_string += string_1[math.floor(element/2)]
        elif element % 2 == 1:
            final_string += string_2[math.floor(element/2)]
        last_index = math.floor(element/2)
    return final_string + largest_string[last_index+1:]

if __name__ == '__main__':
    print(merge_strings('01010111', '000'))
