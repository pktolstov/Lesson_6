"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _lenght = 1
    _width = 1

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width


    def mass_asphalt(self,mass_as, height_cover):
        self.mass_asphalt = mass_as
        self.height_cover = height_cover
        total_mass = (self._lenght * self._width * mass_as * height_cover) / 1000
        print(
            f'Требуется {total_mass} тонн асфальта для прокладки {self._lenght} метров дороги при ширине {self._width} метров')


my_road = Road(5000, 20)
my_road.mass_asphalt(25,5)
