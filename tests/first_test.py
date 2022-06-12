from app.calculator import Calculator


class TestCalc:
    def setup(self):  # предварит. метод в котором подкл-ся тестируемый об-т - калькулятор
        self.calc = Calculator

    def test_multiply_pass(self):  # простой тест на правильность ф-ции
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_pass(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction_pass(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_adding_pass(self):
        assert self.calc.adding(self, 4, 2) == 6


# тестирование без ООП (недостаток: каждый тест запускается отдельно)

def multiply(x, y):  # ф-я которую тестируем
    return x * y


def test_multiply_pass():  # простой тест на корректность ф-ции
    assert multiply(2, 2) == 4


def division(x, y):  # ф-я которую тестируем
    return x / y


def test_division_pass():
    assert division(4, 2) == 2


def subtraction(x, y):  # ф-я которую тестируем
    return x - y


def test_subtraction_pass():
    assert subtraction(4, 2) == 2


def adding(x, y):  # ф-я которую тестируем
    return x + y


def test_adding_pass():
    assert adding(4, 2) == 6