import time

from notes.low_level_design.parking_lot.enum_type import ParkingSpotType, VehicleType
from notes.low_level_design.parking_lot.vechile_type import VehicleFactory
from parking_lot import ParkingLot
from parking_floor import ParkingFloor
from parking_spot import ParkingSpot


# Create Singleton Instance
parking_lot = ParkingLot()

# Add Floors with Parking Spots
floor1 = ParkingFloor(1)
floor1.add_spots(ParkingSpot(101, ParkingSpotType.SMALL))
floor1.add_spots(ParkingSpot(102, ParkingSpotType.MEDIUM))
floor1.add_spots(ParkingSpot(103, ParkingSpotType.LARGE))

floor2 = ParkingFloor(2)
floor2.add_spots(ParkingSpot(201, ParkingSpotType.SMALL))
floor2.add_spots(ParkingSpot(202, ParkingSpotType.MEDIUM))
floor2.add_spots(ParkingSpot(203, ParkingSpotType.LARGE))

parking_lot.add_floor(floor1)
parking_lot.add_floor(floor2)





# Create Vehicles using Factory Pattern
vehicle1 = VehicleFactory.create_vehicle(VehicleType.BIKE, "KA-01-1234")
vehicle2 = VehicleFactory.create_vehicle(VehicleType.CAR, "KA-02-5678")
vehicle3 = VehicleFactory.create_vehicle(VehicleType.TRUCK, "KA-03-9999")

# Park Vehicles
ticket1 = parking_lot.park_vehicle(vehicle1)
ticket2 = parking_lot.park_vehicle(vehicle2)
ticket3 = parking_lot.park_vehicle(vehicle3)

# Display Tickets
print(ticket1)
print(ticket2)
print(ticket3)

# Unpark after some time
time.sleep(2)  # Simulating parking duration
print(parking_lot.unpark_vehicle("KA-01-1234"))
print(parking_lot.unpark_vehicle("KA-02-5678"))
print(parking_lot.unpark_vehicle("KA-03-9999"))

