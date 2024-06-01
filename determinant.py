def det(matrix):
    ln = len(matrix)
    if ln == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    dt = 0
    for i in range(ln):
        mini_matrix = []
        for j in matrix:
            mini_matrix.append(j.copy())
        mini_matrix.remove(mini_matrix[0])
        for j in mini_matrix:
            j[i] = "*"
            j.remove("*")
        dt += ((-1) ** (2 + i)) * det(mini_matrix) * matrix[0][i]
    return dt


