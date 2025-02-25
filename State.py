from enum import Enum

class State(Enum):
    ARRIVED = 1
    VALID_ADDRESS = 2
    DELIVERED = 3
    OUT_FOR_DELIVERY = 4