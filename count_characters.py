def count_characters(lst):
    """Counts how many characters make up a rectangular shape.
    :param lst: list
    :return: int

    """
  return sum(len(i) for i in lst)
