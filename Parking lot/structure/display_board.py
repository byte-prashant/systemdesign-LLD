class DisplayBoard:
  def __init__(self, id):
        self.__id = id
        self.__parking_spots = {}

  # Member functions
  def add_parking_spot(self, spot_type, spots):
    pass
  def show_free_slot(self):
    pass

class ParkinRate:
  def __init__(self, hours, rate):
    self.__hours = hours
    self.__rate = rate

  # Member function
  def calculate(self):
    pass