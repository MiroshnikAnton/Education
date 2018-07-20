
__author__ = 'Мирошник Антон Владимирович'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round(math.sqrt(int(math.fabs(((b_y - a_y) ** 2) + ((b_x - a_x) ** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimeter(self):
        self.perimeter = (self.AB + self.BC + self.CA)
        return (self.perimeter)

    def area(self):
        self.perimeter /= 2
        self.area = round(math.sqrt(self.perimeter*(self.perimeter - self.AB) * (self.perimeter - self.BC) * (self.perimeter - self.CA)), 2)
        return (self.area)

    def height(self):
        self.area *= 2
        self.height = round((self.area / self.CA), 2)
        return (self.height)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

