def inator_inator(inv):
    """Create a function that takes a single word string and does the following:
    - Concatenates inator to the end if the word ends with a consonant, otherwise, concatenate -inator instead.
    - Adds the word length of the original word to the end, supplied with "000".
    """
    length = " " + str(len(inv)) + '000'
    vowels = 'aeiouAEIOU'
    return inv + 'inator' + length if inv[-1] not in vowels else inv + '-inator' + length
