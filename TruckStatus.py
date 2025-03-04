from ClockTime import ClockTime
from State import State

class TruckStatus:
    def __init__(self):
          
        self.trackingHistory = []

    
    # Add a new status and timestamp to the history
    def addToHistory(self, status, time, package=None):
        self.trackingHistory.append((status, time, package))

    # Return the status at or before the specified time.
    def getStatusAt(self, time):
        for status, timestamp, package in reversed(self.trackingHistory):       # TODO add next package (reversed? so previous indx)
            if timestamp <= time:
                return status, package
        return None


        
    
    def __repr__(self):
        trackingHistory_repr = ', '.join([repr(status) for status in self.trackingHistory])
        return f"TruckStatus(trackingHistory=[{trackingHistory_repr}])"