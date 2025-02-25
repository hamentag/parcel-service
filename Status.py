from ClockTime import ClockTime
from enum import Enum

class State(Enum):
    ARRIVED = 1
    VALID_ADDRESS = 2
    DELIVERED = 3
    OUT_FOR_DELIVERY = 4

class Status:
    def __init__(self, deadline, arrivedAt, isValidAddress, addressCorrectedAt):
          
        self.deadline = deadline
       
        self.arrivedAt = arrivedAt

        self.outForDeliveryAt = None

        self.isValidAddress = isValidAddress
        
        self.addressCorrectedAt = addressCorrectedAt

        self.trackingHistory = [(State.ARRIVED, self.arrivedAt), 
                                (State.VALID_ADDRESS, self.addressCorrectedAt)]

    
    # Add a new status and timestamp to the history
    def addToHistory(self, status, timestamp):
        self.trackingHistory.append((status, timestamp))

    # Return the status at or before the specified time.
    def getStatusAt(self, time):
        for status, timestamp in reversed(self.trackingHistory):
            if timestamp <= time:
                return status
        return None 
    


    def isArrivedAt(self, thisTime):
        for status, timestamp in self.trackingHistory:
            if status == "ARRIVED":
                if thisTime < timestamp:
                    return False
                return True
        return False 
    



    # def isArrivedAt(self,thisTime):  
    #     #t = ClockTime(thisTime)
    #     if thisTime.isBefore(self.arrivedAt):
    #         return False
    #     return True

    def isValidAddressAt(self,thisTime):  
        if self.isValidAddress:
            return True
        #t = ClockTime(thisTime)
        if thisTime.isBefore(self.addressCorrectedAt):
            return False
        return True

    def isAvailableAt(self, thisTime):
        return self.isArrivedAt(thisTime) and self.isValidAddressAt(thisTime)
        
    
    def __repr__(self):
        trackingHistory_repr = ', '.join([repr(status) for status in self.trackingHistory])
        return f"Status(arrivedAt={self.arrivedAt}, addressCorrectedAt={self.addressCorrectedAt}, trackingHistory=[{trackingHistory_repr}])"