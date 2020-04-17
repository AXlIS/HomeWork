class Road:
    def __init__(self, lenght, width, mass, hight):
        self.__lenght = lenght
        self.__widht = width
        self.__mass = mass
        self.__hight = hight

    def mass_count(self):
        result = self.__lenght * self.__widht * self.__mass * self.__hight
        print(f'{self.__lenght}м '
              f'* {self.__widht}м '
              f'* {self.__mass}кг '
              f'* {self.__hight}см '
              f'= {result / 1000}т')


road = Road(20, 5000, 25, 5)
road.mass_count()
