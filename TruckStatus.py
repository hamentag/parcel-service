from ClockTime import ClockTime
from State import State
from data.Constants import START_SHIFT

class TruckStatus:
    def __init__(self, truck):
          
        self.trackingHistory = []
        self.addToHistory(State.AT_THE_HUB, START_SHIFT, truck.hub.address_id, truck.mileage)

    
    # Add a new status and timestamp to the history
    def addToHistory(self, status, time, address, mileage, package=None):
        if isinstance(time,ClockTime):
            time = time.get_time_str()
        self.trackingHistory.append((status, time, address, mileage, package))

    ## Return the status at or before the specified time.
    # def getStatusAt(self, time):
    #     for status, timestamp, address, mileage, package  in reversed(self.trackingHistory):
    #         if timestamp <= time:                  
    #             return status, address, mileage, package
    #     return None
    def getStatusAt(self, time):
        if not isinstance(time, ClockTime):
            time = ClockTime(time)
        
        for index, (status, timestamp, address, mileage, package) in enumerate(reversed(self.trackingHistory)):
            if time >= timestamp:
                # Adjust mileage (add the distance traveled between the moment when the last delivery status is recorded and the given time)
                # distance = ClockTime.calculate_distance(time, timestamp, 18.0)
                distance = 0.0 if status == State.AT_THE_HUB else  ClockTime.calculate_distance(time, timestamp, 18.0)
                mileage += distance

                if index > 0:
                    # Get the next (previous in reversed order) address and package
                    next_address = self.trackingHistory[len(self.trackingHistory) - index][2]   # l - index for next element (previous in reversed) and 2 for position of address
                    # next_package = self.trackingHistory[len(self.trackingHistory) - index][4]   # l - index for next element (previous in reversed) and 4 for position of package
                    next_mileage = self.trackingHistory[len(self.trackingHistory) - index][3]   # l - index for next element (previous in reversed) and 4 for position of mileage
                else:
                    next_address =  None  # No next address
                    next_mileage = None  # No next mileage
                return status, address, mileage, package, next_address, next_mileage
        return None
    def is_at_the_hub(self, time):
        status = self.getStatusAt(time)
        return status[0] == State.AT_THE_HUB
        
    
    def __repr__(self):
        trackingHistory_repr = ', '.join([repr(status) for status in self.trackingHistory])
        return f"TruckStatus(trackingHistory=[{trackingHistory_repr}])"