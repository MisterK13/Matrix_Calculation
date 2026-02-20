class MatrixOperations:
    @staticmethod
    def validate_matrix(matrix):
        if not matrix:
            return False, "Матрица не может быть пустой"

        cols = len(matrix[0])
        for row in matrix:
            if len(row) != cols:
                return False, "Все строки матрицы должны иметь одинаковую длину"
            for value in row:
                if not isinstance(value, (int, float)):
                    return False, "Все значения должны быть числами"

        return True, ""

    @staticmethod
    def clean_matrix(matrix):
        if not matrix:
            return matrix

        cleaned = [row for row in matrix if any(val is not None for val in row)]

        if not cleaned:
            return cleaned

        cols_to_remove = []
        for col_index in range(len(cleaned[0])):
            if all(row[col_index] is None for row in cleaned):
                cols_to_remove.append(col_index)

        result = []
        for row in cleaned:
            new_row = [val for index, val in enumerate(row) if index not in cols_to_remove]
            result.append(new_row)

        return result

    @staticmethod
    def add(matrix1, matrix2):
        if len(matrix1) != len(matrix2) or (len(matrix1[0]) != len(matrix2[0])):
            raise ValueError("Матрицы должны иметь одинаковые размеры")

        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)

        return result

    @staticmethod
    def subtract(matrix1, matrix2):
        if len(matrix1) != len(matrix2) or (len(matrix1[0]) != len(matrix2[0])):
            raise ValueError("Матрицы должны иметь одинаковые размеры")

        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] - matrix2[i][j])
            result.append(row)

        return result

    @staticmethod
    def multiply(matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Количество столбцов первой матрицы должно равняться количеству строк второй")

        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                sum_value = 0
                for k in range(len(matrix2)):
                    sum_value += matrix1[i][k] * matrix2[k][j]
                row.append(sum_value)
            result.append(row)

        return result

    @staticmethod
    def determinant(matrix):
        if len(matrix) != len(matrix[0]):
            raise ValueError("Матрица должна быть квадратной")

        n = len(matrix)

        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif n == 3:
            result = (matrix[0][0] * matrix[1][1] * matrix[2][2] +
                      matrix[0][1] * matrix[2][0] * matrix[1][2] +
                      matrix[1][0] * matrix[0][2] * matrix[2][1] -
                      matrix[2][0] * matrix[1][1] * matrix[0][2] -
                      matrix[0][0] * matrix[1][2] * matrix[2][1] -
                      matrix[2][2] * matrix[1][0] * matrix[0][1])
            return result
        else:
            raise ValueError("Максимальный допустимый размер матриц 3*3")


