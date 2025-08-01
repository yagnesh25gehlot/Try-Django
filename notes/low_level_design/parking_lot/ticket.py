import time
import uuid

class Ticket:
    def __init__(self, spot, vehicle):
        self.parking_spot = spot
        self.vehicle = vehicle
        self.ticket_id =  str(uuid.uuid4())[:4]
        self.entry_time = time.time()


    def calculate_fee(self, pricing_strategy, exit_time):
        return pricing_strategy.calculate_fee(self.entry_time, exit_time)