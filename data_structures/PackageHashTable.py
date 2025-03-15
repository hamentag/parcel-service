from data_structures.HashTable import HashTable
from ClockTime import ClockTime
from State import State
from data.Constants import END_SHIFT

class PackageHashTable(HashTable):
    def __init__(self, AddressHashTable):
        super().__init__()
        self.AddressHashTable = AddressHashTable

    #
    def getAllPackageIds(self):
        return super().getAllElementIds()
    
    
    def get_min_deadline(self, time):
        min_deadline = ClockTime(END_SHIFT)
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time) and p.deadline < min_deadline:
                    min_deadline = p.deadline
        return min_deadline
    
    def assign_pcks_with_truck_id(self, time, truck, min_deadline):
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time) and p.truck_id == truck.id and p.deadline == min_deadline:
                    # truck.packages.add(p.id)
                    truck.add_single_package(p.id)
                    p.status.add_to_history(State.EN_ROUTE, time)
      
    
    def getGroupedPackages(self, time, min_deadline):
        package_groups = []   # List to store groups of packages

        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time) and p.deadline == min_deadline:
                    delivered_with = p.delivered_with

                    if len(delivered_with) != 0:
                        delivered_with.add(p.id)

                    # Find an existing group that intersects with the delivered_with set
                    group_found = None
                    for group in package_groups:
                        if not delivered_with.isdisjoint(group):  # Check if there is an intersection
                            group_found = group
                            break

                    if group_found:
                        # Merge the found group with the `delivered_with` set
                        group_found.update(delivered_with)
                    else:
                        # No group found, create a new group
                        package_groups.append(delivered_with)

        # Return the non-empty groups
        return [group for group in package_groups if group]



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
            
    def has_ready_pcks(self, time):
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time):
                    return True
        return False


    # Group packages by their address_id
    def group_by_address_id(self, time):
        address_groups = {}

        # Iterate over all packages in the hash table
        for entry in self.table:
            for p in entry:
                address_id = p.get_address_id(time)
                if address_id not in address_groups:
                    address_groups[address_id] = []
                address_groups[address_id].append(p.id)

        return [group for group in address_groups.values() if len(group) >= 2]
    

    def assign_pck_to_addr(self, time):
         for entry in self.table:
            for p in entry:
                addrId = p.get_address_id(time)
                addr = self.AddressHashTable.lookup(addrId)
                addr.packages.append(p.id)

    
    def get_ready_packages(self, time):
        ready_packages = []
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time):
                    ready_packages.append(p.id)

        return ready_packages
    
    def assign_rem_pcks(self, time, truck,min_deadline):
        for entry in self.table:
            for p in entry:
                if truck.isFull():
                    print("truckkk fullll")
                    print(truck)
                    return
                if p.status.is_ready_at(time) and p.deadline <= min_deadline:
                    truck.add_single_package(p.id)
                    p.status.add_to_history(State.EN_ROUTE, time)
                    p.truck_id = truck.id


    def get_num_delivered_pcks(self, time):
        num_delivered_pcks = 0
        for entry in self.table:
            for p in entry:
                if p.status.is_delivered_at(time):
                    num_delivered_pcks += 1
        return num_delivered_pcks
    
    
    
    
    

    

