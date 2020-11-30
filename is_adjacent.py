def is_adjacent(matrix, node1, node2):
    """ Determine adjacent nodes from matrix
    :param matrix: 2D-array
    :param node1: (int) node1 location
    :param node2: (int) node2 location
    :return: bool
    """
    return matrix[node1][node2] == 1


matrix = [[0, 1, 0, 0],
          [1, 0, 1, 1],
          [0, 1, 0, 1],
          [0, 1, 1, 0]]

print(is_adjacent(matrix, 0, 1))
print(is_adjacent(matrix, 0, 2))

matrix_two = [[0, 1, 0, 1, 1],
              [1, 0, 1, 0, 0],
              [0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1],
              [1, 0, 0, 1, 0]]

print(is_adjacent(matrix, 0, 3))
print(is_adjacent(matrix, 1, 4))
print(is_adjacent(matrix, 3, 2))
