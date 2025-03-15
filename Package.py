from data.Constants import START_SHIFT
class Package:
    def __init__(self, id, address_id, deadline, weight, truck_id, corrected_address_id, address_updated_at, delivered_with, status):
        self.id = id
        self.address_id = address_id
        self.deadline = deadline
        self.weight = weight
        self.truck_id = truck_id
        self.corrected_address_id = corrected_address_id
        self.address_updated_at = address_updated_at
        self.delivered_with = delivered_with
        self.status = status

    def get_address_id(self, time):
        if self.address_updated_at > START_SHIFT and self.status.has_valid_address_at(time):
            return self.corrected_address_id
        return self.address_id

    
    
    def __repr__(self):
        return f"Package(id={self.id}, address_id={self.address_id}, deadline={self.deadline}, " \
        f"weight={self.weight}, truck_id={self.truck_id}, corrected_address_id={self.corrected_address_id}, " \
        f"delivered_with={self.delivered_with}, status={self.status})"
