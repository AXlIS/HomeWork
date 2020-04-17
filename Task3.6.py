class Worker:
    def __init__(self, name, surname, position, wage=None, bonus=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage=None, bonus=None):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.surname} {self.name}')

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


person = Position('Ivan', 'Ivanov', 'doctor', 10000, 1000)
person.get_full_name()
person.get_total_income()
