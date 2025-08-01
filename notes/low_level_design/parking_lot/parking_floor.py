

class ParkingFloor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.parking_spots = []

    def add_spots(self, spot):
        self.parking_spots.append(spot)
        return True

    def get_available_spot(self, spot_type):

        for spot in self.parking_spots:
            if spot.is_available and spot.spot_type.value == spot_type.value:
                return spot


        return None