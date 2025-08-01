import enum_type

class Vehicle:
    def __init__(self, licence_plate, vehicle_type):
        self.licence_plate = licence_plate
        self.vehicle_type = vehicle_type


    def __str__(self):
        return f"{self.licence_plate} - {self.vehicle_type}"

class Car(Vehicle):
    def __init__(self, licence_plate):
        super().__init__(licence_plate, enum_type.VehicleType.CAR)

class Bike(Vehicle):
    def __init__(self, licence_plate):
        super().__init__(licence_plate, enum_type.VehicleType.BIKE)

class Truck(Vehicle):
    def __init__(self, licence_plate):
        super().__init__(licence_plate, enum_type.VehicleType.TRUCK)



class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, licence_plate):
        if vehicle_type.value == enum_type.VehicleType.BIKE.value:
            return Bike(licence_plate)
        elif vehicle_type.value == enum_type.VehicleType.CAR.value:
            return Car(licence_plate)
        elif vehicle_type.value == enum_type.VehicleType.TRUCK.value:
            return Truck(licence_plate)
        else:
            raise ValueError("Vechile type: ", vehicle_type, "is not defined")
