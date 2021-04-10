from homework_02.base import Vehicle


class Car(Vehicle):
    engine = None

    def set_engine(self, engine: object):
        self.engine = engine