from vehicle_type import VehicleType
from vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, vehicle_no):
        super().__init__(vehicle_no, VehicleType.TRUCK)