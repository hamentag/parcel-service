from ClockTime import ClockTime
from State import State

class Status:
    def __init__(self, deadline, arrivedAt, isValidAddress, addressCorrectedAt):
          
        self.deadline = deadline
       
        self.arrivedAt = arrivedAt

        self.outForDeliveryAt = None

        self.isValidAddress = isValidAddress
        
        self.addressCorrectedAt = addressCorrectedAt

        if self.arrivedAt.isBefore(self.addressCorrectedAt):
            self.trackingHistory = [(State.ARRIVED, self.arrivedAt), (State.VALID_ADDRESS, self.addressCorrectedAt), (State.READY, self.addressCorrectedAt)]
        else:
            self.trackingHistory = [(State.VALID_ADDRESS, self.addressCorrectedAt), (State.ARRIVED, self.arrivedAt), (State.READY, self.arrivedAt)]

    
    # Add a new status and timestamp to the history
    def addToHistory(self, status, time):
        self.trackingHistory.append((status, time))

    # Return the status at or before the specified time. 
    def getStatusAt(self, time):
        # print(self.trackingHistory)
        for status, timestamp in reversed(self.trackingHistory):
             if timestamp.isBefore(time): # if timestamp <= time:
                return status
        return None
    
    def is_ready(self, time):
        return self.getStatusAt(time) == State.READY  


    def isArrivedAt(self, time):
        for status, timestamp in self.trackingHistory:
            if status == "ARRIVED":
                if time < timestamp:
                    return False
                return True
        return False 
    



    # def isArrivedAt(self,thisTime):  
    #     #t = ClockTime(thisTime)
    #     if thisTime.isBefore(self.arrivedAt):
    #         return False
    #     return True

    def isValidAddressAt(self,time):  
        if self.isValidAddress:
            return True
        #t = ClockTime(thisTime)
        if time.isBefore(self.addressCorrectedAt):
            return False
        return True

    def isAvailableAt(self, time):
        return self.isArrivedAt(time) and self.isValidAddressAt(time)
        
    
    def __repr__(self):
        trackingHistory_repr = ', '.join([repr(status) for status in self.trackingHistory])
        return f"Status(arrivedAt={self.arrivedAt}, addressCorrectedAt={self.addressCorrectedAt}, trackingHistory=[{trackingHistory_repr}])"