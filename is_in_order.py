def is_in_order(txt):
        """Check whether the string is in order"""

        return txt == "".join(sorted(txt))


print(is_in_order("abc"))