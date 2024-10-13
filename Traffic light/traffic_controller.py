from traffic_light import TrafficLight
from road import Road
from signal import Signal
from threading import Lock
import threading
import time
class TrafficController:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not  cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.roads = {}
            return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()


    def add_road(self, road):
        self.roads[road.id] = road


    def remove_road(self, road_id: str):
        self.roads.pop(road_id, None)


    def start_traffic_control(self):
       for road in self.roads.values():
           traffic_light = road.get_traffic_light()
           threading.Thread(target=self._control_traffic_light, args=(traffic_light,road), daemon=True).start()

       pass


    def _control_traffic_light(self, traffic_light: TrafficLight, road: Road):
        count = 0
        while True:
            try:
                print("road traffic light-------------------", road.id, count)
                #time.sleep(traffic_light.red_duration / 1000)  # Convert to seconds
                traffic_light.change_signal(Signal.GREEN)
                print(traffic_light.get_current_signal())
                #time.sleep(traffic_light.green_duration / 1000)
                traffic_light.change_signal(Signal.YELLOW)
                print(traffic_light.get_current_signal())
                #time.sleep(traffic_light.yellow_duration / 1000)
                traffic_light.change_signal(Signal.RED)
                print(traffic_light.get_current_signal())
                count+=1
            except Exception as e:
                print(f"Error in traffic light control: {e}")


    def handle_emergency(self, road_id: str):
        road = self.roads.get(road_id)
        if road:
            traffic_light = road.get_traffic_light()
            traffic_light.change_signal(Signal.GREEN)
            # Perform emergency handling logic
            # ...

