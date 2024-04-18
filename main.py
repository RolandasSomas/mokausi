from datetime import datetime
from Transport.light_vehicles import Light_vehicles
from Transport.hgv import Hgv
from Transport.bus import Bus
from Transport.transport import Transport

car = Light_vehicles(
    distance_per_year=20000,
    plate_number='ANB205',
    fuel_type='Petrol',
    fixed_cost=4000,
    technical_date= datetime(year=2024, month=7, day=15),
    licence_category='B',
    fuel_consumption= 8,
    insurance_date=datetime(year=2024, month=5, day=15),
)
bus = Bus(
    distance_per_year=28500,
    plate_number='GRJ892',
    fuel_type='Diesel',
    fixed_cost=6000,
    technical_date= datetime(year=2024, month=8, day=27),
    licence_category='D',
    fuel_consumption= 15,
    insurance_date=datetime(year=2024, month=7, day=2),
    seat_amount= 15
)
hgv = Hgv(
    distance_per_year=16800,
    plate_number='LOT166',
    fuel_type='Diesel',
    fixed_cost=8500,
    technical_date=datetime(year=2024, month=8, day=2),
    licence_category='CE',
    fuel_consumption=15,
    insurance_date=datetime(year=2024, month=4, day=3),
    trailer_load_weight= 5
)
# print(car.check_if_next_month_needs_insurance())
# print(car.check_if_next_month_needs_technical())
# print(car.count_cost_of_total_driven_kilometers(100))
print(bus.count_how_many_busses(100))


value = bus.count_how_many_busses(100)
value2 = bus.count_cost_of_total_driven_kilometers(distance=200)
print(value*value2)
hgv.needed_trips_hgv(5)

