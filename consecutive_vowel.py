import re


def vowel_links(txt):
    """Check if there is any word that ends with vowel followed by word starting with vowel"""

    regex = r"\w+([a,e,i,o,u]\s[a,e,i,o,u])\w+"

    return re.findall(regex, txt) != []


one = "an open fire"
two = "the sudden applause"
three = "the large appliances"
four = "creative environment"

print(vowel_links(one))
print(vowel_links(two))
print(vowel_links(three))
print(vowel_links(four))
