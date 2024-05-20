class Date:
    def __init__(self, day, month, year):
        self.set_day(day)
        self.set_month(month)
        self.set_year(year)

    def set_day(self, day):  # Метод установки дня
        if 1 <= day <= 31:
            self.day = day
        else:
            print("Error: Invalid day value")

    def set_month(self, month):  # Метод установки месяца
        if 1 <= month <= 12:
            self.month = month
        else:
            print("Error: Invalid month value")

    def set_year(self, year):  # Метод установки года
        self.year = year

    def get_day(self):  # Метод получения дня
        return self.day

    def get_month(self):  # Метод получения месяца
        return self.month

    def get_year(self):  # Метод получения года
        return self.year

    def print_date_format1(self):  # Метод печати формата "5 января 1997 года"
        month_names = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
        print(f"{self.day} {month_names[self.month - 1]} {self.year} года")

    def print_date_format2(self):  # Метод печати формата "05.01.1997"
        print(f"{self.day:02d}.{self.month:02d}.{self.year}")

# Создание объекта типа Date
date1 = Date(5, 1, 1997)
date1.print_date_format1()  # Вывод: 5 января 1997 года
date1.print_date_format2()  # Вывод: 05.01.1997
