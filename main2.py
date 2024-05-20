class Matrix:
    def __init__(self):
        # Конструктор без параметров
        self.pointer = []  # Указатель на матрицу
        self.rows = 0  # Количество строк
        self.cols = 0  # Количество столбцов
        self.state = 0  # Переменная состояния

    def __init__(self, rows, cols):
        # Конструктор с двумя параметрами - количество строк и столбцов
        self.pointer = [[0 for _ in range(cols)] for _ in range(rows)]  # Выделяет место и инициализирует матрицу нулями
        self.rows = rows
        self.cols = cols
        self.state = 0

    def __del__(self):
        # Деструктор
        del self.pointer

    def get_element(self, i, j):
        # Возвращает значение элемента (i, j)
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.pointer[i][j]
        else:
            self.state = 1
            return None

    def set_element(self, i, j, value):
        # Устанавливает значение элемента (i, j)
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.pointer[i][j] = value
        else:
            self.state = 1

    def print_matrix(self):
        # Функция печати матрицы
        for row in self.pointer:
            print(row)

    def add_matrix(self, other_matrix):
        # Сложение матрицы с другой матрицей
        if self.rows == other_matrix.rows and self.cols == other_matrix.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.pointer[i][j] = self.pointer[i][j] + other_matrix.pointer[i][j]
            return result
        else:
            self.state = 1
            return None

    def sub_matrix(self, other_matrix):
        # Вычитание матрицы из другой матрицы
        if self.rows == other_matrix.rows and self.cols == other_matrix.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.pointer[i][j] = self.pointer[i][j] - other_matrix.pointer[i][j]
            return result
        else:
            self.state = 1
            return None

    def multiply_matrix(self, other_matrix):
        # Умножение матрицы на другую матрицу
        if self.cols == other_matrix.rows:
            result = Matrix(self.rows, other_matrix.cols)
            for i in range(self.rows):
                for j in range(other_matrix.cols):
                    for k in range(self.cols):
                        result.pointer[i][j] += self.pointer[i][k] * other_matrix.pointer[k][j]
            return result
        else:
            self.state = 1
            return None

    def multiply_scalar(self, scalar):
        # Умножение матрицы на скаляр
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.pointer[i][j] = self.pointer[i][j] * scalar
        return result
