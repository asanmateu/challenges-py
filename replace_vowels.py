def replace_vowels(txt, ch):
    """Replace vowels in text with character specified"""

    vowels = "AEIOUaeiou"

    for v in vowels:
        txt = txt.replace(v, ch)

    return txt


print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))

# Alternative pathways:
# Option 1:

import re


def replace_vowels(txt, ch):
    return re.sub(r'[aeiouAEIOU]', ch, txt)


# Option 2:

def replace_vowels(txt, ch):
    return ''.join([i if i not in 'aeoui' else ch for i in txt])
