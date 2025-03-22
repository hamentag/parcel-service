from State import State

##################################################################
# Assigns packages to a truck based on the same delivery address.

def assign_packages_with_same_address(package_hash_table, truck, time):
    # Loop through the truck's current packages to add other packages with the same address
    # # Time Complexity: O(1) where t is the number of packages on the truck. 
    # since t is constant, Time complexity is treated as O(1) relative to n.
    # Space Complexity: O(1).
    for pck in truck.packages.copy():
        if truck.isFull():  # If the truck is full, stop adding more packages
            break
        
        # Get other packages that share the same delivery address as the current package
        packages_in_same_addr = package_hash_table.get_packages_in_same_address(pck, time)
        
        # Create a set of packages that are not already in the truck
        packages_to_add = {item for item in packages_in_same_addr if item not in truck.packages}

        # Check if adding the packages would overload the truck, and if not, add them
        if not truck.is_overloaded_by_adding(len(packages_to_add)):
            # Add the packages to the truck
            package_hash_table.add_multiple_packages(packages_to_add, truck, time)
                   

#########################################################################
# This function manages the process of loading packages with the minimum 
# deadline onto the truck and assigns them to the truck.
# Time Complexity: O(n * t) simplifies to O(n). Space Complexity: O(1)
def loading_packages(package_hash_table, truck, driver, time):

    # Assign packages to their respective addresses
    package_hash_table.assign_pck_to_addr(time)

    # While the truck is not full and there are packages that are ready for delivery
    # Time Complexity: O(n * t) simplifies to O(n). Space Complexity: O(1)
    while not truck.isFull() and package_hash_table.has_ready_pcks(time):

        # Get the minimum deadline package to prioritize it for loading
        min_deadline = package_hash_table.get_min_deadline(time)
        
       # Assign packages that must be delivered on the selected truck and have the minimum deadline.
        package_hash_table.assign_pcks_with_truck_id(time, truck, min_deadline)
       
        # Assign the package with the minimum deadline to the truck, along with any packages
        # that must be delivered together
        package_hash_table.assign_package(time, truck, min_deadline)

        # Assign other packages that have the same address to the truck
        assign_packages_with_same_address(package_hash_table, truck, time)

    # End While
    # Once the truck is full, or there are no more ready packages, finish the loading 
    # process for the current deadline (min_deadline)

    
    # Update the truck's status to "EN_ROUTE" and add it to its history
    truck.status.addToHistory(State.EN_ROUTE, time, truck.hub.address_id, truck.mileage)

    # Allocate the truck to the driver for delivery
    driver.allocate(truck, time)
