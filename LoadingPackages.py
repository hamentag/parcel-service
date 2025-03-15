from State import State

####
def add_multiple_packages(package_hash_table, packages, truck, time):
    for pck_id in packages:
        package = package_hash_table.lookup(pck_id)
        if package and package.status.is_ready_at(time):
            truck.add_single_package(pck_id)
            package.status.add_to_history(State.EN_ROUTE, time)
            package.truck_id = truck.id
        else:
            print(f"Package {pck_id} not found or not ready at {time}.")
######
def assign_grouped_packages(package_hash_table, package_sets, truck, time):
    i = 0   
    while i < len(package_sets) and package_hash_table.has_ready_pcks(time):
        if not truck.is_overloaded_by_adding(len(package_sets[i])):
            add_multiple_packages(package_hash_table, package_sets[i], truck, time)           
            
        i += 1
#####
def assign_packages_with_same_address(package_hash_table, truck, time):
    package_hash_table.assign_pck_to_addr(time)
    ### add pcks in the same addr
    for pck in truck.packages.copy():
        if truck.isFull():
            break
        
        packages_in_same_addr = package_hash_table.get_packages_in_same_address(pck, time)

        packages_to_add = {item for item in packages_in_same_addr if item not in truck.packages}
        if not truck.is_overloaded_by_adding(len(packages_to_add)):
            add_multiple_packages(package_hash_table, packages_to_add, truck, time)
                   

################################

################################
def loading_packages(package_hash_table, truck, driver, time):
    while not truck.isFull() and package_hash_table.has_ready_pcks(time):
        min_deadline = package_hash_table.get_min_deadline(time)
        
        # ######## Assign packages to trucks (Must be delivered with #, #, ..)
        # O(n)
        package_hash_table.assign_pcks_with_truck_id(time, truck, min_deadline)

        ##
        groups = package_hash_table.getGroupedPackages(time,min_deadline)
        assign_grouped_packages(package_hash_table, groups, truck, time)

        ##
        assign_packages_with_same_address(package_hash_table, truck, time)


        ## Rem
        if not truck.isFull():
            package_hash_table.assign_rem_pcks(time, truck,min_deadline)
    # End While
    #    

    ####
    truck.status.addToHistory(State.EN_ROUTE, time)
    driver.allocate(truck, time)
    