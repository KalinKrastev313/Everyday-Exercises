class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if not len(self.customers) == MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvds(self, dvd):
        if not len(self.dvds) == MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    