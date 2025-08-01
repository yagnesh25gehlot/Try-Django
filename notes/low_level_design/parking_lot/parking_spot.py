



class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_available = True
        self.vehicle = None

    def park_vehicle(self, vehicle):
        if not self.is_available:
            return False
        self.is_available = False
        self.vehicle = vehicle
        return True

    def unpark_vehicle(self):
        self.is_available = True
        self.vehicle = None


    def __str__(self):
        status = 'Available' if self.is_available else 'Not Available'
        return f"Spot id: {self.spot_id}, parked vehicle: {self.vehicle.name}, status: {status}"
