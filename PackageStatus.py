from ClockTime import ClockTime
from State import State

class PackageStatus:
    def __init__(self, deadline, arrived_at, addressCorrectedAt):
        self.deadline = deadline
        self.arrived_at = arrived_at
        self.addressCorrectedAt = addressCorrectedAt
        self.trackingHistory = []
        
        if self.addressCorrectedAt >= self.arrived_at:
            self.add_all_to_history([(State.ARRIVED, self.arrived_at), (State.VALID_ADDRESS, self.addressCorrectedAt), (State.READY, self.addressCorrectedAt)])
        else:
            self.add_all_to_history([(State.VALID_ADDRESS, self.addressCorrectedAt), (State.ARRIVED, self.arrived_at), (State.READY, self.arrived_at)])
       

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
    def is_delivered_at(self, time):
        return self.getStatusAt(time) == State.DELIVERED
    
    def is_en_route_at(self, time):
        return self.getStatusAt(time) == State.EN_ROUTE

    def has_valid_address_at(self, time):
        for status, timestamp in self.trackingHistory:
            if status == State.VALID_ADDRESS:
                return time >= timestamp
        return False
    
    def get_delivery_time(self):
        for status, timestamp in reversed(self.trackingHistory):
            if status == State.DELIVERED:
                return timestamp
        return None
    
    def get_en_route_time(self):
        for status, timestamp in reversed(self.trackingHistory):
            if status == State.EN_ROUTE:
                return timestamp
        return None
    
    def get_ready_time(self):
        for status, timestamp in reversed(self.trackingHistory):
            if status == State.READY:
                return timestamp
        return None

    def is_ready_at(self, time):
        return self.getStatusAt(time) == State.READY
    
    def __repr__(self):
        trackingHistory_repr = ', '.join([repr(status) for status in self.trackingHistory])
        return f"Status(trackingHistory=[{trackingHistory_repr}])"