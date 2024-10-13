from vehicle_type import VehicleType
from abc import ABC

class Vehicle(ABC):

    def __init__(self, vehicle_no, vehicle_type : VehicleType):
        self.vehicle_no = vehicle_no
        self.vehicle_type = VehicleType.CAR