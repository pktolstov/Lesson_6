"""
5. Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import task_4

towncar = task_4.TownCar(61, 'blue', 'VW')
print(f'Атрибуты экземпляра подкласса TownCar: {towncar.name}, {towncar.speed}, {towncar.color}, {towncar.is_police}')
towncar.show_speed()
towncar.go()
towncar.stop()
towncar.turn('налево')

bolid = task_4.SportCar(161, 'red', 'AUDI R8')
print(f'Атрибуты экземпляра подкласса SportCar: {bolid.name}, {bolid.speed}, {bolid.color}, {bolid.is_police}')
bolid.show_speed()
bolid.go()
bolid.stop()
bolid.turn('направо')

commerce_car = task_4.WorkCar(41, 'yellow', 'JCB')
print(
    f'Атрибуты экземпляра подкласса WorkCar: {commerce_car.name}, {commerce_car.speed}, {commerce_car.color}, {commerce_car.is_police}')
commerce_car.show_speed()
commerce_car.go()
commerce_car.stop()
commerce_car.turn('направо')

police = task_4.PoliceCar(90, 'white', 'Police Buick')
print(f'Атрибуты экземпляра подкласса PoliceCar: {police.name}, {police.speed}, {police.color}, {police.is_police}')
police.show_speed()
police.go()
police.stop()
police.turn('налево')
