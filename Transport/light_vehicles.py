from datetime import datetime, timedelta
from Transport.transport import Transport

class Light_vehicles(Transport):
    def __init__(self, distance_per_year: int, plate_number: str, fuel_type: str, insurance_date: datetime,
                 technical_date: datetime, fixed_cost, licence_category, fuel_consumption):

        super().__init__(distance_per_year, plate_number, fuel_type, insurance_date, technical_date, fixed_cost,
                         licence_category, fuel_consumption)



