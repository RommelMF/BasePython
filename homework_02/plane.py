from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):


    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        Vehicle.__init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, number):
        current_cargo = self.cargo + number
        if current_cargo <= self.max_cargo:
            self.cargo = current_cargo
        else:
            raise CargoOverload('Overload!')

    def remove_all_cargo(self):
        source_cargo = self.cargo
        self.cargo = 0
        return source_cargo