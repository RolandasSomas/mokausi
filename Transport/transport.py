from datetime import datetime, timedelta


class Transport:

    def __init__(
        self,
        distance_per_year: int,
        plate_number: str,
        fuel_type: str,
        insurance_date: datetime,
        technical_date: datetime,
        fixed_cost: int = 0,
        licence_category: str = "b",
        fuel_consumption: float = 8.5,
    ):
        self.insurance_date = insurance_date
        self.fuel_consumption = fuel_consumption
        self.licence_category = licence_category
        self.technical_date = technical_date
        self.fixed_cost = fixed_cost
        self.fuel_type = fuel_type
        self.plate_number = plate_number
        self.distance_per_year = distance_per_year

    def __check_next_month(self, date: datetime):
        today = datetime.today()
        next_month = today.replace(day=1) + timedelta(35)
        two_month_next = today.replace(day=1) + timedelta(65)

        if datetime(year=next_month.year, month=next_month.month, day=1) <= date < datetime(
            year= two_month_next.year, month=two_month_next.month, day=1):
            return True
        return False

    def check_if_next_month_needs_technical(self):
        if self.__check_next_month(self.technical_date):
            return True
        return False

    def check_if_next_month_needs_insurance(self):
        if self.__check_next_month(self.insurance_date):
             return True
        return False

    def count_cost_of_total_driven_kilometers(self,distance:int, fuel_price=1.5):
        return self.fuel_consumption * fuel_price/ 100 + (self.fixed_cost / self.distance_per_year) * distance