from State import State
from utils.DistanceDataReader import read_distance


def update_current_pcks_status(package_hash_table, hub, truck, time, current_location):
        if current_location != hub.address_id:
            for pck in truck.packages:
                package = package_hash_table.lookup(pck)
                if package is not None and package.get_address_id(time) == current_location:
                    package.status.add_to_history(State.DELIVERED, time)
                    truck.status.addToHistory(State.FINISHED_DELIVERING, time, pck)

            ## filter remaining packages
            truck.packages = {pck for pck in truck.packages if not package_hash_table.lookup(pck).status.is_delivered_at(time)}

def get_remaining_addr_distances(package_hash_table, truck, time, current_location):
    addr_distances = []
    package_addresses = {package_hash_table.lookup(pck).get_address_id(time) for pck in truck.packages}

    for adrss in package_addresses:
        addr_distances.append((adrss, read_distance(current_location, adrss)))

    return addr_distances
        
def return_to_the_hub(hub, truck, time, current_location):

    #### Return to the Hub
    # distance_to_hub = distance_hash_table.lookup(current_location, hub.address_id)
    from utils.DistanceDataReader import read_distance
    distance_to_hub = read_distance(current_location, hub.address_id)
    print(",,,distance to return o hub ,,,")
    print(distance_to_hub)

    truck.mileage += distance_to_hub

    # Calculate time to reach destination in minutes (distance / speed in miles per hour)
    time_to_travel_minutes = (distance_to_hub / truck.speed) * 60
    time.add_travel_time(time_to_travel_minutes)

    truck.status.addToHistory(State.AT_THE_HUB, time)


def get_nearest_location(addr_distances):
    nearest_location = addr_distances[0]
    for addr_distance in addr_distances:
        if addr_distance[1] <= nearest_location[1]:
            nearest_location = addr_distance

    return nearest_location



def executing_delivery(package_hash_table, hub, truck, time):
    
    current_location = hub.address_id
            
    done = False
    while not done:

        update_current_pcks_status(package_hash_table, hub, truck, time, current_location)
                
        
        addr_distances = get_remaining_addr_distances(package_hash_table, truck, time, current_location)

        if len(addr_distances) == 0:
            truck.status.addToHistory(State.RETURNING_TO_THE_HUB, time)
            done = True
        else:
            nearest_location = get_nearest_location(addr_distances)  # tuple (20, 1.9)
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

    ### Return to the Hub
    return_to_the_hub(hub, truck, time, current_location)

    print(f"----time--- end_of_delivery_day = {time.get_time_str()}")
