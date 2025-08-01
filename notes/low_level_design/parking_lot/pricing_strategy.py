from abc import ABC, abstractmethod





class PricingStrategy(ABC):

    @abstractmethod
    def calculate_fee(self, entry_time, exit_time):
        pass



class FixedPriceStrategy(PricingStrategy):
    def __init__(self, fixed_price):
        self.fixed_price = fixed_price

    def calculate_fee(self, entry_time, exit_time):
        t = max(  1, (exit_time-entry_time)/3600 )
        return round(t*self.fixed_price, 2)



fixed_price_strategy = FixedPriceStrategy(fixed_price=5)