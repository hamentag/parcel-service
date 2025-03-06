from State import State

class DeliveryProcess:
    def __init__(self, package_hash_table, distance_hash_table, hub):
        self.package_hash_table = package_hash_table
        self.distance_hash_table = distance_hash_table
        self.hub = hub
    
    def execute(self, truck, time):
        current_location = self.hub.address_id
               
        done = False
        while not done:
            if current_location != self.hub.address_id:
                for pck in truck.packages:
                    package = self.package_hash_table.lookup(pck)
                    if package is not None and package.addressId == current_location:
                        package.status.add_to_history(State.DELIVERED, time)
                        truck.status.addToHistory(State.FINISHED_DELIVERING, time, pck)

                ## filter remaining packages
                truck.packages = {pck for pck in truck.packages if self.package_hash_table.lookup(pck).addressId != current_location}       


            package_addresses = {self.package_hash_table.lookup(pck).addressId for pck in truck.packages}

            sorted_distances = self.distance_hash_table.get_sorted_distances(current_location, package_addresses)
            if len(sorted_distances) == 0:
                truck.status.addToHistory(State.RETURNING_TO_THE_HUB, time)

                # next_location = None
                done = True
            else:
                nearest_location = sorted_distances.pop(0)       # tuple (20, 1.9)
                next_location = nearest_location[0]
                distance = nearest_location[1]
                truck.mileage += distance

                # Calculate time to reach destination in minutes (distance / speed in miles per hour)
                time_to_travel_minutes = (distance / truck.speed) * 60
                time.add_travel_time(time_to_travel_minutes)

                # last_location = current_location
                current_location = next_location
                # current_time = arrival_time
        
        print ("end While")

        
        #### print
        print('current_location')
        print(current_location)
        print('next_location')
        print(next_location)
        # print('last_location') 
        # print(last_location) 
        # print('current_time')
        # print(current_time)

        print('time')
        print(time)

        print(truck.mileage)


   

        #### Return to the Hub
        distance_to_hub = self.distance_hash_table.lookup(current_location, self.hub.address_id)
        print(",,,distance to return o hub ,,,")
        print(distance_to_hub)

        truck.mileage += distance_to_hub

        # Calculate time to reach destination in minutes (distance / speed in miles per hour)
        time_to_travel_minutes = (distance_to_hub / truck.speed) * 60
        time.add_travel_time(time_to_travel_minutes)

        truck.status.addToHistory(State.AT_THE_HUB, time)

        
        print('time after returning to hub')
        print(time)
        print(truck.mileage)
        
        

        # stop


        