"""
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    is_police:bool

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        #self.is_police = False

    def go(self):
        print(f'автомобиль {self.name} начал движение')

    def stop(self):
        print(f'автомобиль {self.name} остановился')

    def turn(self, direction):
        self.direction = direction
        print(f'автомобиль {self.name} повернул {self.direction}')

    def show_speed(self):
        print(f'скорость {self.name} {self.speed}')


class TownCar(Car):
    Car.is_police=False


    def show_speed(self):
        if self.speed <= 60:

            Car.show_speed(self)
        else:
            print('Вы превысили скорость!')


class SportCar(Car):
    Car.is_police = False





class WorkCar(Car):
    Car.is_police=False
    #def __init__(self, speed, color, name):

        #super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed <= 40:

            Car.show_speed(self)
        else:
            print('Вы превысили скорость!')


class PoliceCar(Car):
    Car.is_police=True
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


#car1 = TownCar(61, 'blue', 'VW')
#car1.show_speed()
#car1.go()
#car1.stop()
#car1.turn('left')

#car2 = SportCar(161, 'red', 'AUDI R8')
#car2.show_speed()
#car2.go()
##car2.turn('right')

#car3 = WorkCar(41, 'yellow', 'JCB')
#car3.show_speed()
#car3.go()
#car3.stop()
#car3.turn('right')

#car4 = PoliceCar(90, 'yellow', 'Police Buick')
#car4.show_speed()
#car4.go()
#car4.stop()
#car4.turn('right')
