class Topping:
    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        self.__topping_type = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Should be pos")
        self.__weight = value


t = Topping("a", -2)
print(t.weight)
t.weight = -3