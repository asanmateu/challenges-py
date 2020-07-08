def is_isogram(txt):
    """ is the word an isogram"""
    clean_word = txt.lower()
    letter_list = []
    for letter in clean_word:
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)

    return True


print(is_isogram('Algorithm'))