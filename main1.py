class Vector:
    def __init__(self):
        # Конструктор без параметров
        self.pointer = [0]  # Выделяет место для одного элемента и инициализирует его в ноль
        self.num_elements = 1
        self.state = 0  # Переменная состояния

    def __init__(self, size):
        # Конструктор с одним параметром - размер вектора
        self.pointer = [i for i in range(size)]  # Выделяет место и инициализирует элементами от 0 до size-1
        self.num_elements = size
        self.state = 0

    def __init__(self, size, value):
        # Конструктор с двумя параметрами
        self.pointer = [value for _ in range(size)]  # Выделяет место и инициализирует элементами значением value
        self.num_elements = size
        self.state = 0

    def __del__(self):
        # Деструктор освобождает память
        del self.pointer

    def set_element(self, index, value=0):
        # Функция, присваивающая элементу массива значение (по умолчанию 0)
        if index < 0 or index >= self.num_elements:
            self.state = 1  # Устанавливает код ошибки, если выходит за пределы массива
        else:
            self.pointer[index] = value

    def get_element(self, index):
        # Функция, возвращающая элемент массива
        if index < 0 or index >= self.num_elements:
            self.state = 1
            return None
        return self.pointer[index]

    def print_vector(self):
        # Функция печати
        print(self.pointer)

    def __add__(self, other):
        # Операция сложения двух векторов
        result = Vector(self.num_elements)
        for i in range(self.num_elements):
            result.pointer[i] = self.pointer[i] + other
        return result

    def __mul__(self, other):
        # Операция умножения вектора на число
        result = Vector(self.num_elements)
        for i in range(self.num_elements):
            result.pointer[i] = self.pointer[i] * other
        return result

    def __sub__(self, other):
        # Операция вычитания числа из вектора
        result = Vector(self.num_elements)
        for i in range(self.num_elements):
            result.pointer[i] = self.pointer[i] - other
        return result

    def __eq__(self, other):
        # Операция сравнения на равенство
        return self.pointer == other.pointer

    def __lt__(self, other):
        # Операция сравнения "меньше чем"
        return self.num_elements < other.num_elements

    def __gt__(self, other):
        # Операция сравнения "больше чем"
        return self.num_elements > other.num_elements

    @classmethod
    def count_objects(cls):
        # Подсчет числа объектов данного типа
        return cls.num_objects
