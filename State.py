from enum import Enum

class State(Enum):
    ARRIVED = 1
    VALID_ADDRESS = 2
    DELIVERED = 3
    EN_ROUTE = 4
    AT_THE_HUB = 5
    READY = 6
    FINISHED_DELIVERING = 7     # For trucks
    RETURNING_TO_THE_HUB = 8


    def __repr__(self):
            return self.name
