"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод
"""
import time


class TrafficLight:
    __color = 'цвет'

    def running(self):
        while True:
            tmp = {'краный': 7, 'желтый': 2, 'зеленый': 4}
            for key in tmp.keys():
                print(key)
                time.sleep(tmp[key])

street_light = TrafficLight()
street_light.running()