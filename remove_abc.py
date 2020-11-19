def remove_abc(txt):
    """Removes letters "a", "b", and "c" from a given string and return modified version
    Args:
        txt(string): string to be modified
    Returns:
        txt(string): transformed string
        """
    if any((c in txt) for c in ('a', 'b', 'c')):
        txt = txt.replace('a', '').replace('b', '').replace('c', '')
        return txt
    else:
        return None

print(remove_abc("This might be a bit hard"))
print(remove_abc("Hello world!"))
print(remove_abc("Coding is fun!"))
