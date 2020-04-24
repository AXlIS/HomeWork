class Clothing:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def coat_size(self):
        result = self.v / 6.5 + 0.5
        return round(result, 1)

    def jacket_size(self):
        result = self.h * 2 + 3
        return round(result, 1)

    @property
    def full(self):
        result = (self.v / 6.5 + 0.5) + (self.h * 2 + 3)
        print(round(result, 1))


clothing = Clothing(7, 5)
print(clothing.jacket_size())
print(clothing.coat_size())
clothing.full
