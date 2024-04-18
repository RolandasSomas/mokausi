from datetime import datetime, timedelta
from Transport.transport import Transport
from math import ceil


class Hgv(Transport):
    def __init__(self, distance_per_year: int, plate_number: str, fuel_type: str, insurance_date: datetime,
                 technical_date: datetime, fixed_cost: int = 0, licence_category: str = "b",
                 fuel_consumption: float = 8.5, trailer_load_weight : int=0, trailer_needed: bool = True, hgv_carried_weight:int=12):
        self.trailer_load_weight = trailer_load_weight
        self.trailer_needed = trailer_needed
        self.hgv_carried_weight = hgv_carried_weight
        super().__init__(distance_per_year, plate_number, fuel_type, insurance_date, technical_date, fixed_cost,
                         licence_category, fuel_consumption)

    def needed_trips_hgv(self, total_weight:int):
        truck = int
        truck = ceil(total_weight / (self.hgv_carried_weight + self.trailer_load_weight))
        trailer= int
        trailer = ceil((total_weight - self.hgv_carried_weight * truck) / truck)
        print(trailer)


'''
Paskaičiuoti kiek reisų reikia padaryti ir ar reikia prikabinti priekabą (tarkim reikia pervežti 30, automobilio pervežamas svoris yra 12 tonų, priekabos pervežamas svoris 5 tonos. Tokiu atveju reikia vieną karta vežti be priekabos, o antra su priekaba. Bet jei reikia pervežti tarkime 36 tonos, priekabos kabinti neverta, nes vistiek reikia daryti tris reisus)'''





