from datetime import datetime, timedelta
from Transport.transport import Transport
import math



class Bus(Transport):
    def __init__(self, distance_per_year: int, plate_number: str, fuel_type: str, insurance_date: datetime,
                 technical_date: datetime, fixed_cost: int = 0, licence_category: str = "b",
                 fuel_consumption: float = 8.5, seat_amount: int=0):
        super().__init__(distance_per_year, plate_number, fuel_type, insurance_date, technical_date, fixed_cost,
                         licence_category, fuel_consumption)
        self.seat_amount = seat_amount

    # Metodas, kiek reikia autobusų norint pervežti N keleivių;
    def count_how_many_busses(self, given_passenger_number:int=100):
        try:
            return math.ceil(given_passenger_number / self.seat_amount)
        except ZeroDivisionError as e:
            print(f'Klaida:{e}')

# Paskaičiuotų kokia būtų bendra samata pervežus N keleivių ir nuvažiavus X kilometrų.




