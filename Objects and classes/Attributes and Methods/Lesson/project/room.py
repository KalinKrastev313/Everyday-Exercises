class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    @staticmethod
    def can_be_taken(self, is_taken, people, capacity):
        return not is_taken and people <= capacity

    def take_room(self, people):
        if not self.can_be_taken(self.is_taken, people, self.capacity):
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests = people

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.guests = 0
        self.is_taken = False

