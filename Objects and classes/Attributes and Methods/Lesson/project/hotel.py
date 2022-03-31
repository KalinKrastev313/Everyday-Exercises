class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def find_room(rooms, room_number):
        return list(filter(lambda room: room.room_number == room_number, rooms))[0]

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        result = self.find_room(self.rooms, room_number).take_room(people)

        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        guests_to_remove = self.find_room(self.rooms, room_number)
        result = self.find_room(self.rooms, room_number).free_room()
        if result:
            return result
        self.guests -= guests_to_remove





