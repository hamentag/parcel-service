from State import State

#####
def assign_packages_with_same_address(package_hash_table, truck, time):
    # package_hash_table.assign_pck_to_addr(time)
    ### add pcks in the same addr
    for pck in truck.packages.copy():
        if truck.isFull():
            break
        
        packages_in_same_addr = package_hash_table.get_packages_in_same_address(pck, time)

        packages_to_add = {item for item in packages_in_same_addr if item not in truck.packages}
        if not truck.is_overloaded_by_adding(len(packages_to_add)):
            # add_multiple_packages(package_hash_table, packages_to_add, truck, time)
            package_hash_table.add_multiple_packages(packages_to_add, truck, time)
                   

################################
def loading_packages(package_hash_table, truck, driver, time):

    package_hash_table.assign_pck_to_addr(time)

    while not truck.isFull() and package_hash_table.has_ready_pcks(time):
        min_deadline = package_hash_table.get_min_deadline(time)
        
        # ######## Assign packages to trucks (Must be delivered with #, #, ..)
        # O(n)
        package_hash_table.assign_pcks_with_truck_id(time, truck, min_deadline)


        package_hash_table.assign_package(time, truck, min_deadline)
        assign_packages_with_same_address(package_hash_table, truck, time)

    # End While
    
    ####
    truck.status.addToHistory(State.EN_ROUTE, time, truck.hub.address_id, truck.mileage)
    driver.allocate(truck, time)
    