from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=1300, fuel=40, fuel_consumption=0.00):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is not True and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError('Not fuel!')

    def move(self, distance):
        consumption = distance * self.fuel_consumption
        if self.fuel >= consumption:
            self.fuel -= consumption
        else:
            raise NotEnoughFuel('Not enough fuel!')
