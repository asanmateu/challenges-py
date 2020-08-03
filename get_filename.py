def get_filename(path):
    """Create a function which returns the selected filename from a path.
    Include the extension in your answer."""

    return path.split('/')[-1]


print(get_filename("C:/Projects/pil_tests/ascii/toni.txt"))
