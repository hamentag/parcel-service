from State import State
from utils.DistanceDataReader import read_distance

# Updates the status of packages on the truck that have been delivered at the current location.
# Time Complexity: O(1), Space Complexity: O(1) 
def update_current_pcks_status(package_hash_table, hub, truck, time, current_location):
        if current_location != hub.address_id:
            for pck in truck.packages:
                package = package_hash_table.lookup(pck)
                if package is not None and package.get_address_id(time) == current_location:
                    package.status.add_to_history(State.DELIVERED, time)
                    truck.status.addToHistory(State.FINISHED_DELIVERING, time, current_location, truck.mileage, pck)

              # Filter remaining packages (those not delivered yet)
            truck.packages = {pck for pck in truck.packages if not package_hash_table.lookup(pck).status.is_delivered_at(time)}


# Retrieves the distances to all remaining addresses where the truck still needs to deliver packages.
# Time Complexity: O(m), Space Complexity: O(1)
def get_remaining_addr_distances(package_hash_table, truck, time, current_location):
    addr_distances = []
    package_addresses = {package_hash_table.lookup(pck).get_address_id(time) for pck in truck.packages}

    # Retrieve the distance for each address
    # Time complexity: O(m * k), where m is the total number of addresses and k is the number of addresses 
    # corresponding to the current truck's packages. It simplifies to O(m) since k is much smaller than m.
    for addr in package_addresses:
        addr_distances.append((addr, read_distance(current_location, addr)))

    return addr_distances

# Handles the return of the truck to the hub after completing deliveries.
# Time Complexity: O(m), Space Complexity: O(1)     
def return_to_the_hub(hub, truck, time, current_location):

    # Return to the Hub
    # Time Complexity: O(m)
    from utils.DistanceDataReader import read_distance
    distance_to_hub = read_distance(current_location, hub.address_id)
    
    truck.mileage += distance_to_hub

    # Calculate time to reach destination in minutes (distance / speed in miles per hour)
    time_to_travel_minutes = (distance_to_hub / truck.speed) * 60
    time.add_travel_time(time_to_travel_minutes)

    truck.status.addToHistory(State.AT_THE_HUB, time, hub.address_id, truck.mileage)

# Finds the nearest address to the current location based on the distances.
# Time Complexity: O(1), Space Complexity: O(1) 
def get_nearest_location(addr_distances):
    nearest_location = addr_distances[0]
    for addr_distance in addr_distances:
        if addr_distance[1] <= nearest_location[1]:
            nearest_location = addr_distance

    return nearest_location


#########################################################################
# Executes the entire delivery process for the truck
# Time Complexity: O(1), Space Complexity: O(1) 
def executing_delivery(package_hash_table, hub, truck, time):
    
    current_location = hub.address_id
            
    done = False
    while not done:
        # Update the status of the packages that have been delivered at the current location
        update_current_pcks_status(package_hash_table, hub, truck, time, current_location)
                
        # Get the remaining address distances for delivery
        addr_distances = get_remaining_addr_distances(package_hash_table, truck, time, current_location)

        if len(addr_distances) == 0:
            # If all deliveries are done, mark the truck as returning to the hub
            truck.status.addToHistory(State.RETURNING_TO_THE_HUB, time, current_location, truck.mileage)
            done = True
        else:
            # Find the nearest address and update the truck's location
            nearest_location = get_nearest_location(addr_distances)  # tuple (address_id, distance)
            next_location = nearest_location[0]
            distance = nearest_location[1]
            truck.mileage += distance

            # Calculate time to travel to the next location
            time_to_travel_minutes = (distance / truck.speed) * 60
            time.add_travel_time(time_to_travel_minutes)

            # Update current location to the next nearest address
            current_location = next_location
    
    # End While

    # Return the truck to the hub after all deliveries
    return_to_the_hub(hub, truck, time, current_location)
