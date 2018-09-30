def extract_max_recursion(a_string):
    """
    Here, +1 for an open parenthesis, -1 for a closing one.
    We keep a track of the value in a counter, the maximum value taken
    by this counter is the maximum recursion level.
    """
    counter = 0
    maximum = 0
    for character in a_string:
        if character == ')':
            counter -= 1
            if counter > maximum:
                maximum = counter
        elif character == '(':
            counter += 1
            if counter > maximum:
                maximum = counter
    return maximum

if __name__ == '__main__':
    assert extract_max_recursion('(kfds(fds)fdsfsd)ffdsfs') == 2
    assert extract_max_recursion('(((()())))') == 4
