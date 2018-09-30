def get_opening_closing_indexes(a_string):
    """
    Getting the closing index of an opening index.  
    """
    stack = []
    position_dict = {}
    for index, character in enumerate(a_string):
        if character == '(':
            stack.append(index)
        if character == ')':
            element = stack.pop()
            position_dict[element] = index
    return position_dict

if __name__ == '__main__':
    print(get_opening_closing_indexes('(re(fdsfs)fdsfsdfsd)'))

