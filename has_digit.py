import re


def has_digit(txt):
    return bool(re.search(r'\d', txt))


print(has_digit("c8"))
print(has_digit("23cc4"))
print(has_digit("abwekz"))
