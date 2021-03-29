"""
6. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title: str):
        self.title = title
    def draw(self):
        print(f'Инструмент: {self.title}. Родительский класс! Запуск отрисовки!')
class Pen(Stationery):
    def draw(self):
        print(f'Инструмент: {self.title}. Запуск отрисовки!')
class Pencil(Stationery):
    def draw(self):
        print(f'Инструмент: {self.title}. Запуск отрисовки!')
class Handle(Stationery):
    def draw(self):
        print(f'Инструмент: {self.title}. Запуск отрисовки!')

parent_class=Stationery('Инструмент родительского класса')
parent_class.draw()

new_pen=Pen('Шариковая ручка')
new_pen.draw()

new_pencil=Pencil('Карандаш Kohinoor')
new_pencil.draw()

new_hadle=Handle('Красный маркер')
new_hadle.draw()


