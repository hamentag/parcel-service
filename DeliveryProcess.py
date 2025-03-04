from State import State

class DeliveryProcess:
    def __init__(self, package_hash_table, distance_hash_table, hub):
        self.package_hash_table = package_hash_table
        self.distance_hash_table = distance_hash_table
        self.hub = hub
    
    def fct(self, truck, time):
        current_location = 0
        # last_location = current_location
        current_time = time

        # for pck in truck.packages:
        #     p = self.package_hash_table.lookup(pck)
        #     print(",,,self.package_hash_table.lookup(pck).addressId")
        #     print(p)
        #     print(self.package_hash_table.lookup(pck).addressId)

        while True:
            if current_location != 0:
                for pck in truck.packages:
                    package = self.package_hash_table.lookup(pck)
                    if package is not None and package.addressId == current_location:
                        package.status.addToHistory(State.DELIVERED, current_time)
                        truck.status.addToHistory(State.FINISHED_DELIVERING, current_time, pck)

                print(',,,truck,,,,')
                print(truck)

                ## delete pck
                truck.packages = {pck for pck in truck.packages if self.package_hash_table.lookup(pck).addressId != current_location}       

                print(',,,truck, deleted itm,,,')
                print(truck)
            
            
            package_addresses = {self.package_hash_table.lookup(pck).addressId for pck in truck.packages}

            sorted_distances = self.distance_hash_table.get_sorted_distances(current_location, package_addresses)
            print(",,,sorted_dist,,,")
            print(sorted_distances)
            print(len(sorted_distances))
            if len(sorted_distances) == 0:
                # next_location = None
                break
            
            nearest_location = sorted_distances.pop(0)       # tuple (20, 1.9)
            next_location = nearest_location[0]
            distance = nearest_location[1]
            truck.mileage += distance

            # Calculate time to reach destination in minutes (distance / speed in miles per hour)
            time_to_travel_minutes = (distance / truck.speed) * 60
            arrival_time = current_time.get_arrival_time(time_to_travel_minutes)

            # last_location = current_location
            current_location = next_location
            current_time = arrival_time


                ######
            # last_location = current_location            
            # current_location = next_location
            # current_time = arrival_time
        
        print ("end While")


        stop
      




    



        