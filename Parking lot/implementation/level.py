from parking_spots import ParkingSpots
from typing import List
from  vehicle_type import VehicleType
from  vehicle import Vehicle

class Level:

    def __init__(self, floor, no_of_spots):
        self.floor  = floor
        self.spots: List[ParkingSpots] = [ParkingSpots(spot_no) for spot_no in range(1, no_of_spots+1)]


    def park_vehicle(self, vehicle: Vehicle):
        for spot in self.spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.vehicle_type:
                print("parked vehicle successfully")
                spot.park_vehicle(vehicle)
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                print("unparked vehicle successfully")
                return True
        return False

    def display_availability(self) -> None:
        print(f"Level {self.floor} Availability:")
        for spot in self.spots:
            print(f"Spot {spot.get_spot_number()}: {'Available' if spot.is_available() else 'Occupied'}")
