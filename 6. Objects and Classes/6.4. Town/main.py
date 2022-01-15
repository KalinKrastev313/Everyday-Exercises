class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = None
        self.longitude = None

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

# how to print " " in print function
town = Town("Sofia")
town.set_latitude("42° 41\ 51.04\&quot; N&quot;")
town.set_longitude("&quot;23° 19\&#39; 26.94\&quot; E&quot;")
print(town)