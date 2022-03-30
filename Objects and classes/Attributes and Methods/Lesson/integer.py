import math


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if type(value) != float:
            return "value is not a float"
        return cls(math.floor(value))

    @classmethod
    def from_roman(cls, value):
        pass

    @classmethod
    def from_string(cls, value):
        if type(value) != str:
            return "wrong type"
        return cls(int(value))

    def add(self, integer):
        return self.value + integer.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")
second_num = Integer(15)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))