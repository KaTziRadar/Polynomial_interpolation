#adar katzir 209502293
import math
def Polynomial_Interpolation (table, xf):
    y_vactor = []
    x_vector = []
    result_vector = []
    for key in table:
        x_vector.append(key)
        y_vactor.append([table[key]])

    result_mat = CalcMatrix(create_matrix(x_vector), y_vactor)
    for col in result_mat:
        result_vector.append(col[0])

    return create_polinom(result_vector)(xf)

def create_polinom(param_list):
    def polinom(x):
        pow = 0
        val = 0
        for param in param_list:
            val += param * math.pow(x, pow)
            pow += 1
        return val
    return polinom

def create_matrix(x_list):
    i = 0
    pow = 0
    n = len(x_list)
    mat = [([0] * n) for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            mat[i][j] = math.pow(x_list[i], pow)
            pow += 1
        pow = 0
    return mat

def CalcMatrix(matrix, b):
    return Matrix_multiplication(InvertMatrix(matrix), b)


def Matrix_multiplication(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        raise Exception("Illegal multiplication between matrix's ")
    result_mat = [([0] * len(mat2[0])) for i in range(len(mat1))]  # initialize the result matrix with zeros

    # iterate through the first matrix rows
    for row1 in range(0, len(mat1)):
        # iterate through the second matrix columns
        for col2 in range(0, len(mat2[0])):
            # iterate through the second matrix rows
            for row2 in range(0, len(mat2)):
                result_mat[row1][col2] += mat1[row1][row2] * mat2[row2][col2]
    return result_mat
def Identity(n):
    mat = [([0] * n) for i in range(n)]
    for i in range(0, n):
        mat[i][i] = 1
    return mat
def InvertMatrix(matrix):
    if len(matrix) != len(matrix[0]):
        raise Exception("singular matrix. there is no inverted matrix")
    n = len(matrix)
    inverted = Identity(n)
    for j in range(0, n):
        for i in range(0, n):
            if i == j:
                pivot = matrix[i][j]
                for k in range(i + 1, n):
                    if abs(matrix[k][j]) > abs(pivot):  # pivoting
                        elementary_matrix = ExchangeRows(k, i, n)
                        matrix = Matrix_multiplication(elementary_matrix, matrix)
                        inverted = Matrix_multiplication(elementary_matrix, inverted)
                        pivot = matrix[i][j]

                if matrix[i][j] == 0:
                    raise Exception("singular matrix. there is no inverted matrix")

        for i in range(0, n):
            if i != j:
                if matrix[i][j] != 0:
                    elementary_matrix = ResetOrgan(i, j, n, pivot, matrix[i][j])
                    matrix = Matrix_multiplication(elementary_matrix, matrix)
                    inverted = Matrix_multiplication(elementary_matrix, inverted)

    for i in range(0, n):
        if matrix[i][i] != 1:
            if matrix[i][i] < 0:
                elementary_matrix = MultiplyRow(i, -1, n)
                matrix = Matrix_multiplication(elementary_matrix, matrix)
                inverted = Matrix_multiplication(elementary_matrix, inverted)

            elementary_matrix = MultiplyRow(i, 1 / matrix[i][i], n)
            matrix = Matrix_multiplication(elementary_matrix, matrix)
            inverted = Matrix_multiplication(elementary_matrix, inverted)
    for row in range(n):
        for col in range(n):
            inverted[row][col] = round(inverted[row][col], 2)
    return inverted

def ResetOrgan(row, col, n, pivot, a):
    elementary_matrix = Identity(n)
    elementary_matrix[row][col] = -(a / pivot)
    return elementary_matrix

def MultiplyRow(row, a, n):
    elementary_matrix = Identity(n)
    elementary_matrix[row][row] = a
    return elementary_matrix

def ExchangeRows(row1, row2, n):
    elementary_matrix = Identity(n)
    elementary_matrix[row1][row1] = 0
    elementary_matrix[row1][row2] = 1
    elementary_matrix[row2][row2] = 0
    elementary_matrix[row2][row1] = 1
    return elementary_matrix

table = {0.35 :-213.5991 ,0.4:-204.4416 ,0.55:-194.9375,0.65 :-185.0256,0.7 :-174.6711,0.85 :-163.8656,0.9 :-152.6271}
x = 0.75
print(Polynomial_Interpolation(table,x))