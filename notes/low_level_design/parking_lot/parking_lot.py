from notes.low_level_design.parking_lot.ticket import Ticket
from pricing_strategy import FixedPriceStrategy
import time


class ParkingLot:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls._instance.floors = []
            cls._instance.active_tickets = {}
            cls._instance.pricing_strategy = FixedPriceStrategy(fixed_price=10)

        return cls._instance

    def add_floor(self, floor):
        self.floors.append(floor)

    def find_spot_for_vehicle(self, vehicle):
        for floor in self.floors:
            spot = floor.get_available_spot(vehicle.vehicle_type)
            if spot:
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_spot_for_vehicle(vehicle)
        if spot:
            spot.park_vehicle(vehicle)
            ticket = Ticket(spot, vehicle)
            self.active_tickets[vehicle.licence_plate] = ticket
            return ticket
        return None


    def unpark_vehicle(self, licence_plate):
        if licence_plate in self.active_tickets:
            ticket = self.active_tickets[licence_plate]
            exit_time = time.time()
            price = ticket.calculate_fee(self.pricing_strategy, exit_time)
            ticket.parking_spot.unpark_vehicle()
            return f"{price}"
