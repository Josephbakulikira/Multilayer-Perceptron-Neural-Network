import random
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for i in range(cols)] for j in range(rows)]
        #or you can simply use numpy
        """
        # import numpy as np
        # self.matrix = np.zeros((rows,cols))
        """

    def multiply(self, value):
        if type(value) is Matrix:
            #check if the we can multiply the two matrix
            if self.cols == value.rows:
                result = Matrix(self.rows, value.cols)
                for x in range(result.rows):
                    for y in range(result.cols):
                        sum = 0
                        for z in range(self.cols):
                            sum += self.matrix[x][z] * value.matrix[z][y]
                        result.matrix[x][y] = sum
                return result

            else:
                print("the number of column of the first matrix must be equal to the number of rows in the second matrix, error!")
        else:
            for x in range(self.rows):
                for y in range(self.cols):
                    self.matrix[x][y] *= value

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for x in range(self.rows):
            for y in range(self.cols):
                result.matrix[y][x] = self.matrix[x][y]
        return result

    def add(self, value):
        if type(value) is Matrix:
            for x in range(self.rows):
                for y in range(self.cols):
                    self.matrix[x][y] += value.matrix[x][y]
        else:
            for x in range(self.rows):
                for y in range(self.cols):
                    self.matrix[x][y] += value

    def HadamartProduct(self, value):
        for x in range(self.rows):
            for y in range(self.cols):
                self.matrix[x][y] *= value.matrix[x][y]

    def __add__(self, _matrix):
        mat = Matrix(self.rows, self.cols)
        for x in range(self.rows):
            for y in range(self.cols):
                mat.matrix[x][y] = self.matrix[x][y] + _matrix.matrix[x][y]
        return mat

    def randomize(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.matrix[x][y] = random.randint(0, 10)

    def map(self, fn):
        #apply a function for every element in the matrix
        for x in range(self.rows):
            for y in range(self.cols):
                self.matrix[x][y] = fn(self.matrix[x][y])

    def matrix_multiplication(a, b):
        columns_a = len(a[0])
        rows_a = len(a)
        columns_b = len(b[0])
        rows_b = len(b)

        result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
        if columns_a == rows_b:
            for x in range(rows_a):
                for y in range(columns_b):
                    sum = 0
                    for k in range(columns_a):
                        sum += a[x][k] * b[k][y]
                    result_matrix[x][y] = sum
            return result_matrix

        else:
            print("columns of the first matrix must be equal to the rows of the second matrix")
            return None
m1 = Matrix(2, 3)
m1.matrix=[[2, 3, 4],[5, 4, 2]]
m2 = Matrix(3, 2)
m2.matrix = [[9, 4], [3, 2], [5,6]]


#
# m1.matrix = Matrix.matrix_multiplication(m1.matrix, m2.matrix)
# m1 = m1.multiply(m2)
print(m1.matrix)
#print(m1.rows)
# print(m1.cols)
