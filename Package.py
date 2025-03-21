from data.Constants import START_SHIFT
class Package:
    def __init__(self, id, address_id, deadline, weight, corrected_address_id, address_updated_at, truck_id_requirement, delivered_with, status):
        self.id = id                    # Unique identifier for the package
        self.address_id = address_id    # The ID of the address where the package is to be delivered
        self.deadline = deadline        # The deadline by which the package must be delivered
        self.weight = weight
        self.truck_id = -1        # The truck ID on which the package is currently delivered
        self.corrected_address_id = corrected_address_id
        self.address_updated_at = address_updated_at        # Timestamp of when the address was last updated
        self.truck_id_requirement = truck_id_requirement    # The truck ID that the package is required to be on according to business rules
        self.delivered_with = delivered_with
        self.status = status                    # The delivery status of the package

    def get_address_id(self, time):
        if self.address_updated_at > START_SHIFT and self.status.has_valid_address_at(time):
            return self.corrected_address_id
        return self.address_id

    
    def __repr__(self):
        return f"Package(id={self.id}, address_id={self.address_id}, deadline={self.deadline}, " \
        f"weight={self.weight}, truck_id={self.truck_id}, corrected_address_id={self.corrected_address_id}, " \
        f"address_updated_at={self.address_updated_at}, delivered_with={self.delivered_with}, status={self.status})"
