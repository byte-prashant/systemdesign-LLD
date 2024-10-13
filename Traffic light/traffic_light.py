from  signal import Signal
from threading import Lock


class TrafficLight:

    def __init__(self, id, red_duration, green_duration, yellow_duration):

        self.yellow_duration = yellow_duration
        self.id = id

        self.green_duration = green_duration
        self.red_duration = red_duration
        self.current_signal = Signal.RED



    def change_signal(self, new_signal):
        #with Lock:
        self.current_signal = new_signal
        self.notify_observer()

    def get_current_signal(self):
        return self.current_signal


    def notify_observer(self):

        # can we use observer pattern here to automatically
        # inform the observers about the change

        pass
