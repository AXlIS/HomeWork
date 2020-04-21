class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn_right(self):
        print('Машина повернула на право')

    def turn_left(self):
        print('Машина повернула налево')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('Это полицейская машина')


ferarri = SportCar(200, 'red', 'ferarri', False)
print(ferarri.name)
vaz = WorkCar(60, 'black', 'vaz', False)
vaz.show_speed()
