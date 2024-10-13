from vehicle_type import  VehicleType
from vehicle import Vehicle

class ParkingSpots:

    def __init__(self, spot_no):
        self.spot_number = spot_no
        self.parked_vehicle = None
        self.vehicle_type  = VehicleType.CAR



    def is_available(self):
        if not self.parked_vehicle:
            return True

        return False


    def park_vehicle(self,vehicle:Vehicle):

        if self.is_available() and self.vehicle_type == vehicle.vehicle_type:
            self.parked_vehicle = vehicle
            print("veicle parked")

        else:
            raise ValueError("Invalid vehicle type or spot already occupied.")

    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None

    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type

    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle

    def get_spot_number(self) -> int:
        return self.spot_number