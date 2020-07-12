def format_ascii(txt, width):
    """Given a very long string of ASCII characters, split the string up into equal
    sized groups of size width. To properly display the image, join up the groups with
    the newline character \n and return the output string."""

    return "\n".join(txt[i:i + width] for i in range(0, len(txt), width))

print(format_ascii('0123456789', 2))