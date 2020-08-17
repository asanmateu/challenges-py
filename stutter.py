def stutter(word):
    """ Write a function that stutters a word as if someone is struggling to read it.

    :param word: str
    :return: str
    """
    return str(2 * (word[:2] + '... ') + word + '?')


print(stutter('outstanding'))
