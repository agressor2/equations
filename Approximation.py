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


def permute(arr, memo=None):
    if memo is None:
        memo = []
    results = []
    for i in range(len(arr)):
        cur = arr.pop(i)
        if len(arr) == 0:
            results.append(memo + [cur])
        results += permute(arr[:], memo + [cur])
        arr.insert(i, cur)
    return results


A = [[1, 0, 1, 2], [0, 1, 4, 3], [0, 2, 1, 0], [0, 0, 1, 1]]
b = [1, 2, 3, 4]


def equation(A, b, c, eps):
    A = permute(A)
    max_diagonal_summ = [0, 0]
    for i in range(len(A)):
        diagonal_summ = 0
        for j in range(len(A[i])):
            diagonal_summ += abs(A[i][j][j])
        if max_diagonal_summ[0] < abs(diagonal_summ):
            max_diagonal_summ = [abs(diagonal_summ), i]
    c = permute(c)[max_diagonal_summ[1]]
    A = A[max_diagonal_summ[0]]

    if det(A) == 0:
        return "Нет корней", "Нет корней", "Нет корней"
    condition = True
    print(c)
    variables0 = [0 for i in c]

    while condition:
        for i in range(len(b)):
            variables0[i] = c[i]
        for i in range(len(c)):
            form = 0
            for j in range(len(c)):
                if j != i:
                    form -= A[i][j] * c[j]
            c[i] = (b[i] + form) / A[i][i]

        print(variables0)
        if max(abs(c[i] - variables0[i]) for i in range(len(c))) <= eps or str(c[0]) == 'nan':
            condition = False
        # break
    if str(c[0]) == 'nan':
        return 'Привышено максимальное значение', 'Привышено максимальное значение', 'Привышено максимальное значение'
    return [str(c[i]) + ' ± ' + str(eps) for i in range(len(c))]


print(equation(A, b, [0, 0, 0, 0], 0))
