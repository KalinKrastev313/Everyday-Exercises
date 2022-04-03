import movieworld.custommer


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

    def rent_dvd(self, customer_id, dvd_id):
        for dvd in self.dvds:
            if dvd.is_rented is True:
                for customer in self.customers:
                    if dvd in customer.rented_dvds:
                        if customer.id == customer_id:
                            return f"{customer.name} has already rented {dvd.name}"
                        elif not customer.id == customer_id:
                            return "DVD is already rented"
            else:
                for customer in self.customers:
                    if customer_id == customer.id:
                        if not customer.age >= dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        else:
                            




        # for customer in self.customers:
        #     if customer.id == customer_id:
        #         for dvd in customer.rented_dvds:
        #             if dvd.id == dvd_id:
        #                 return f"{customer.name} has already rented {dvd.name}"


