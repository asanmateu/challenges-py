def replace_vowels(txt, ch):
    """Replace vowels in text with character specified"""

    vowels = "AEIOUaeiou"

    for v in vowels:
        txt = txt.replace(v, ch)

    return txt


print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))

