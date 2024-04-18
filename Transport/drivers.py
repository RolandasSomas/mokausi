'''
Vairuotojas, kuris turi atributus:

Atostogų laikas

Turima teisių kategorija (D sukvežimiai be priekabos, E su priekaba)

Darbo užmokestis vienam kilometrui;
'''
import datetime
class Driver():
    def __init__(self, holiday_time):
        # self.driver_category = driver_category
        self.holiday_time = holiday_time

    def has_holiday(self, date):
        for start_date, end_date in self.holiday_time:
            if start_date <= date <= end_date:
                return True
        return False
driver_holidays = [
    (datetime.date(2024, 4, 1), datetime.date(2024, 4, 5)),
    (datetime.date(2024, 5, 20), datetime.date(2024, 5, 25))
]
date_to_check = datetime.date(2024, 4, 3)
driver = Driver(driver_holidays)
if driver.has_holiday(date_to_check):
    print(f" has a holiday on {date_to_check}.")
else:
    print(f" does not have a holiday on {date_to_check}.")
print(driver_holidays)
