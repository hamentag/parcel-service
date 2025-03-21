from ClockTime import ClockTime
from State import State
from data.Constants import START_SHIFT

class PackageStatus:
    def __init__(self, deadline, arrived_at, addressCorrectedAt):
        self.deadline = deadline
        self.arrived_at = arrived_at
        self.addressCorrectedAt = addressCorrectedAt
        self.trackingHistory = []
        
        if self.addressCorrectedAt >= self.arrived_at:
            self.add_all_to_history([(State.AT_THE_HUB, self.arrived_at), (State.VALID_ADDRESS, self.addressCorrectedAt), (State.READY, self.addressCorrectedAt)])
        else:
            self.add_all_to_history([(State.VALID_ADDRESS, self.addressCorrectedAt), (State.AT_THE_HUB, self.arrived_at), (State.READY, self.arrived_at)])
       

    # Add a new status and timestamp to the history
    def add_to_history(self, status, time):
        self.trackingHistory.append((status, time.get_time_str()))

    def add_all_to_history(self, status_time_list):
        for status, time in status_time_list:
            self.add_to_history(status, time)

    # Return the status at a specified time.
    def getStatusAt(self, time):
        if isinstance(time, str):
            time = ClockTime(time)
        for status, timestamp in reversed(self.trackingHistory):
            if time >= timestamp:
                return status
        return None
    
    def get_status_in_range(self, t1, t2):
        if isinstance(t1, str):
            t1 = ClockTime(t1)
        if isinstance(t2, str):
            t2 = ClockTime(t2)
        if t2 < t1:
            t1, t2 = t2, t1
        status_list = [(self.getStatusAt(t2), t2.get_time_str())]
        for status, timestamp in reversed(self.trackingHistory):
            if t2 < timestamp:
                continue
         
            if t1 >= timestamp:
                status_list.append((status, t1.get_time_str()))
                break
            status_list.append((status, timestamp))
      
        return status_list[::-1]       #Reverse list back
    def is_delivered_at(self, time):
        return self.getStatusAt(time) == State.DELIVERED
    
    def is_delivered_by_time(self, deadline):
        delivery_time = self.get_delivery_time()
        if delivery_time is not None:
            return self.get_delivery_time() <= deadline
        return False
    
    def is_en_route_at(self, time):
        return self.getStatusAt(time) == State.EN_ROUTE
    def is_delayed(self):
        return self.arrived_at > START_SHIFT
        
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