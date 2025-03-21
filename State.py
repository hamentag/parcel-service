from enum import Enum

class State(Enum):
    # For packages
    AT_THE_HUB = 1      # For both packages and trucks
    VALID_ADDRESS = 2
    READY = 3
    EN_ROUTE = 4
    DELIVERED = 5
   
    # For trucks
    FINISHED_DELIVERING = 6     # For trucks
    RETURNING_TO_THE_HUB = 7


    def __repr__(self):
            return self.name
