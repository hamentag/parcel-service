from data_structures.HashTable import HashTable
from ClockTime import ClockTime
from State import State
from data.Constants import END_SHIFT

class PackageHashTable(HashTable):
    def __init__(self, AddressHashTable):
        super().__init__()
        self.AddressHashTable = AddressHashTable

    #
    def get_all_package_ids(self):
        return super().get_all_element_ids()
    
    
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
                if p.status.is_ready_at(time) and p.truck_id_requirement == truck.id and p.deadline == min_deadline:
                    # truck.packages.add(p.id)
                    truck.add_single_package(p.id)
                    p.status.add_to_history(State.EN_ROUTE, time)
                    p.truck_id = truck.id
      
    
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
    

    def assign_pck_to_addr(self, time):
         for entry in self.table:
            for p in entry:
                addrId = p.get_address_id(time)
                addr = self.AddressHashTable.lookup(addrId)
                addr.packages.add(p.id)

    
    def get_ready_packages(self, time):
        ready_packages = []
        for entry in self.table:
            for p in entry:
                if p.status.is_ready_at(time):
                    ready_packages.append(p.id)

        return ready_packages
    

 
    def collect_packages(self):
        for entry in self.table:
            for p in entry:
                set_delivered_with = p.delivered_with
                if len(set_delivered_with) != 0:
                    set_delivered_with.add(p.id)
                    for p_id in set_delivered_with:         # Max = TRUCK_MAX_CAPACITY = 16
                        package = self.lookup(p_id)
                        package.delivered_with.update(set_delivered_with)
                   
    
    
    def add_multiple_packages(self, packages, truck, time):
        for pck_id in packages:
            package = self.lookup(pck_id)
            if package and package.status.is_ready_at(time):
                truck.add_single_package(pck_id)
                package.status.add_to_history(State.EN_ROUTE, time)
                package.truck_id = truck.id
                
    
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

    def get_num_delivered_pcks(self, time):
        num_delivered_pcks = 0
        for entry in self.table:
            for p in entry:
                if p.status.is_delivered_at(time):
                    num_delivered_pcks += 1
        return num_delivered_pcks

   