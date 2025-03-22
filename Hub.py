class Hub:
    HUB_ADDRESS_ID = 0
    def __init__(self, name, package_hash_table, address_id=HUB_ADDRESS_ID):
        self.name = name
        self.address_id = address_id
        self.package_hash_table = package_hash_table
        self.trucks = []
        self.end_of_delivery_day = None
                
    # Select the truck with the minimum mileage among those currently at the hub
    # Time Complexity: O(t). where t is the number of truks. Since t is a constant much smaller 
    # than n (number of packages), overall time complexity is O(1)
    # Space Complexity: O(t), and it is also treated as O(1) relative to n 
    def selectTruckWithMinMileage(self, time):
        # Create a list of trucks that are currently at the hub at the given time
        trucks_at_hub = [truck for truck in self.trucks if truck.status.is_at_the_hub(time)]

        # Initialize the first truck in the list as the one with the minimum mileage
        minTruck = trucks_at_hub[0]

        # Iterate through the list of trucks to find the one with the minimum mileage
        for truck in trucks_at_hub:
            if truck.mileage < minTruck.mileage:
                minTruck = truck    # Update minTruck 
          
        # Return the truck with the minimum mileage
        return minTruck
  


    def trucks_total_mileage(self):
        total = 0
        for truck in self.trucks:
            total += truck.mileage
        return total

    def __repr__(self):
        trucks_repr = ', '.join([repr(truck) for truck in self.trucks])
        return f"Hub(name={self.name}, address_id={self.address_id}, end_of_delivery_day={self.end_of_delivery_day} trucks=[{trucks_repr}])"
