#########################################################
# Repository: https://github.com/hamentag/parcel-service

#########################################################
## For Time and Space Complexity:
# n: The number of packages.
# m: The number of addresses.

#########################################################
from data_structures.HashTable import HashTable
from ClockTime import ClockTime
from State import State
from data.Constants import END_SHIFT

class PackageHashTable(HashTable):
    # calls the parent constructor and stores the given AddressHashTable
    # Time Complexity: O(1), Space Complexity: O(1)
    def __init__(self, AddressHashTable):
        super().__init__()
        self.AddressHashTable = AddressHashTable

    # Retrieves the IDs of all the packages in the hash table.
    # Time Complexity: O(n), Space Complexity: O(n) (Time Complexity and Space Complexity of the get_all_element_ids() function)
    def get_all_package_ids(self):
        return super().get_all_element_ids()
    
    # Finds the package with the earliest deadline that is ready at the given time
    # Returns: the earliest deadline for any package ready at the given time.
    # Time Complexity: O(n), (Num of entries x Num of packages in each entry)
    # Space Complexity: O(1)
    def get_min_deadline(self, time):
        min_deadline = ClockTime(END_SHIFT)
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time) and p.deadline < min_deadline:
                    min_deadline = p.deadline
        return min_deadline
    
    # Assigns packages that are ready at the given time and match the minimum deadline to the given truck.
    # Time Complexity: O(n), Space Complexity: O(1)
    def assign_pcks_with_truck_id(self, time, truck, min_deadline):
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time) and p.truck_id_requirement == truck.id and p.deadline == min_deadline:
                    # truck.packages.add(p.id)
                    truck.add_single_package(p.id)
                    p.status.add_to_history(State.EN_ROUTE, time)
                    p.truck_id = truck.id
      
    #  Returns all the packages that are at the same address as the specified package at the given time.
    #  Time Complexity: O(m), Space Complexity: O(1)
    def get_packages_in_same_address(self, package_id, time):
        package = self.lookup(package_id)
        if package:
            address = self.AddressHashTable.lookup(package.get_address_id(time))
            if address:
                return address.packages
            else:
                print(f"Address {package.get_address_id(time)} not found.")
        else:
            print(f"Package {package_id} not found.")

    # Checks if there are any packages ready to be assigned at the given time.
    # Time Complexity: O(n), Space Complexity: O(1)
    def has_ready_pcks(self, time):
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time):
                    return True
        return False
    

    # Assigns all packages to their respective addresses at the given time.
    # Time Complexity: O(n), Space Complexity: O(1)
    def assign_pck_to_addr(self, time):
         for entry in self.table:
            for p in entry:
                addrId = p.get_address_id(time)
                addr = self.AddressHashTable.lookup(addrId)
                addr.packages.add(p.id)

    # Retrieves a list of all the ready package IDs at the given time.
    # Time Complexity: O(n), Space Complexity: O(n)
    def get_ready_packages(self, time):
        ready_packages = []
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time):
                    ready_packages.append(p.id)

        return ready_packages
    

    # Collects all the packages that must be delivered with other packages.
    # Updates the delivered_with sets for the collected packages.
    # Time Complexity: O(n), Space Complexity: O(n)
    def collect_packages(self):
        for entry in self.table:
            for p in entry:
                set_delivered_with = p.delivered_with
                if len(set_delivered_with) != 0:
                    set_delivered_with.add(p.id)
                    for p_id in set_delivered_with:         # Max = TRUCK_MAX_CAPACITY = 16
                        package = self.lookup(p_id)
                        package.delivered_with.update(set_delivered_with)
                   
    
    # Adds multiple packages to a truck if they are ready at the given time
    # Time Complexity: 
        # O(1) for each call since the function operates on a constant c : number of packages (up to 16)
        # Number of calls = n / c 
        # Overall time complexity is O(n / c) * O(1) which simplifies to O(n).
    # Space Complexity: O(1)
    def add_multiple_packages(self, packages, truck, time):
        for pck_id in packages:
            package = self.lookup(pck_id)
            if package and package.status.is_ready_at(time):
                truck.add_single_package(pck_id)
                package.status.add_to_history(State.EN_ROUTE, time)
                package.truck_id = truck.id
                
    # Assign the package with the minimum deadline to the truck, along with any packages in p.delivered_with
    # (packages that must be delivered together). If the truck cannot accommodate all the packages,
    # the entire set is deferred to the next truck that has enough capacity.
    # Time Complexity: O(n), Space Complexity: O(1)
    def assign_package(self, time, truck, min_deadline):
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time) and p.deadline <= min_deadline:
                    truck.add_single_package(p.id)
                    p.status.add_to_history(State.EN_ROUTE, time)
                    p.truck_id = truck.id
                    if len(p.delivered_with) != 0 and not truck.is_overloaded_by_adding(len(p.delivered_with)):
                        self.add_multiple_packages(p.delivered_with, truck, time)
                    return
    
    # Retrieves the number of packages that have been delivered at the given time.
    # Time Complexity: O(n), Space Complexity: O(1)
    def get_num_delivered_pcks(self, time):
        num_delivered_pcks = 0
        for entry in self.table:
            for p in entry:
                if p.status.is_delivered_at(time):
                    num_delivered_pcks += 1
        return num_delivered_pcks
