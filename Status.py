from ClockTime import ClockTime
from State import State

class Status:
    def __init__(self, deadline, arrivedAt, addressCorrectedAt):
          
        self.deadline = deadline
       
        self.arrivedAt = arrivedAt

        self.addressCorrectedAt = addressCorrectedAt

        self.trackingHistory = []
        
        
        if self.addressCorrectedAt >= self.arrivedAt:
            self.add_all_to_history([(State.ARRIVED, self.arrivedAt), (State.VALID_ADDRESS, self.addressCorrectedAt), (State.READY, self.addressCorrectedAt)])
           
        else:
            self.add_all_to_history([(State.VALID_ADDRESS, self.addressCorrectedAt), (State.ARRIVED, self.arrivedAt), (State.READY, self.arrivedAt)])
       

    
    # Add a new status and timestamp to the history
    def add_to_history(self, status, time):
        self.trackingHistory.append((status, time.get_time_str()))

    def add_all_to_history(self, status_time_list):
        for status, time in status_time_list:
            self.add_to_history(status, time)

    # Return the status at a specified time.
    def getStatusAt(self, time):
        for status, timestamp in reversed(self.trackingHistory):
            if time >= timestamp:
                return status
        return None
    def get_delivery_time(self):
        for status, timestamp in reversed(self.trackingHistory):
            if status == State.DELIVERED:
                return timestamp
        print("None,,,," )
        return None


    def is_ready(self, time):
        return self.getStatusAt(time) == State.READY          
    
    def __repr__(self):
        trackingHistory_repr = ', '.join([repr(status) for status in self.trackingHistory])
        return f"Status(trackingHistory=[{trackingHistory_repr}])"