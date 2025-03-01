class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.capacity = capacity

school_bus = Bus(max_speed=110, mileage=197, capacity=35)
print(f"Максимальная скорость автобуса: {school_bus.max_speed}")
print(f"Пробег автобуса: {school_bus.mileage}")
print(f"Вместимость автобуса: {school_bus.capacity}")