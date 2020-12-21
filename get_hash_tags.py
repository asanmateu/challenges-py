import re


def get_hash_tags(txt):
    """Retrieves the top 3 longest words of a newspaper headline and transforms them into hashtags."""

    words = sorted(re.findall(r"\w+", txt), key=len, reverse=True)

    return ['#' + word.lower() for word in words][:3]


print(get_hash_tags("How the Avocado Became the Fruit of the Global Trade"))
print(get_hash_tags("Why You Will Probably Pay More for Your Christmas Tree This Year"))
print(get_hash_tags("Visualizing Science"))