from State import State
# from utils.Quicksorter import Quicksorter
from utils.Quicksorter import sort
class Loader:
    def __init__(self, packageHashTable, hub):
        self.packageHashTable = packageHashTable
        self.hub = hub
    
    def assign_constrained_packages(self, truck, time):
        #### Apply business requirements defined in project notes
        for package_id in self.hub.packages:
            package = self.packageHashTable.lookup(package_id)
            if not truck.isFull() and package is not None and package.truckId == truck.id and package.status.is_ready(time):
                print("tstt ,,,, valid")                 
                truck.add_single_package(package_id)
                self.hub.packages.remove(package_id)
                # change status to out for delivery
                package.status.add_to_history(State.EN_ROUTE, time)
                truck.packages.add(package_id)

    
    def get_deadline(self, package_id):
            package = self.packageHashTable.lookup(package_id)
            if package is not None:
                return package.deadline
            
    # Get the earliest deadline : the sorting criterion for the outer list
    def get_earliest_deadline(self, set_pck_ids):
        # Convert set to a list and sort the inner list
        list_pck_id = list(set_pck_ids)
        sort(list_pck_id, 0, len(list_pck_id) - 1, self.get_deadline)
        
        # return the deadline of the first elment of the sorted inner list (earliest deadline)
        package = self.packageHashTable.lookup(list_pck_id[0])
        if package is not None:
            return package.deadline
    
    def assign_package_sets(self, package_sets, truck, time):
        i = 0           
        while i < len(package_sets) and not truck.is_overloaded_by_adding(len(package_sets[i])) and not self.hub.isEmpty():
            all_ready = all(self.packageHashTable.lookup(pck_id).status.is_ready(time) for pck_id in package_sets[i])
            if not all_ready:
                i += 1
                continue
            
            for pck_id in package_sets[i]:
                package = self.packageHashTable.lookup(pck_id)
                if package: 
                    truck.add_single_package(pck_id)
                    self.hub.packages.remove(pck_id)
                    package.status.add_to_history(State.EN_ROUTE, time)
                else:
                    print(f"Package {pck_id} not found.")
            
            i += 1
    

    def assign_grouped_packages(self, truck, time):
        ########## print
        print('hub.get_grouped_packages(packageHashTable)')
        print(self.hub.get_grouped_packages())

        grouped_packages = self.hub.get_grouped_packages()

        # ##### sort       

        # ds = [30, 8, 9, 31, 32]     # [31, 30, 32, 8, 9]
        # ds2 = [[30, 37, 29], [8,40, 4], [31, 5], [9, 33], [32, 37, 38]]

        

        # print("unnnsort tsttt ,, ds = ,,,")
        # print(ds)

        # sort(ds, 0, len(ds) - 1, self.get_deadline)
        # print("sort tsttt ,, ds = ,,,")
        # print(ds)

        # print("unnnsort tsttt ,, ds2 = ,,,")
        # print(ds2)

        # sort(ds2, 0, len(ds2) - 1, self.get_earliest_deadline)
        # print("sort tsttt ,, ds2 = ,,,")
        # print(ds2)

        # # apply
        # grouped_packages.append({2,3,4})
        # grouped_packages.append({5,6,7})

        print("unnnsorted ,, grouped_packages = ,,,")
        print(grouped_packages)
        sort(grouped_packages, 0, len(grouped_packages) - 1, self.get_earliest_deadline)
        print("sorted ,, grouped_packages = ,,,")
        print(grouped_packages)

        self.assign_package_sets(grouped_packages, truck, time)
    
    
    def assign_pcks_with_similar_address(self, truck, time):
        package_lists = self.hub.groups_pcks_with_similar_address()        # arg .. attribute?
        
        print(',, start test here,,,,, unsorted ,,, groups_pcks_with_similar_address')
        print(package_lists)

        sort(package_lists, 0, len(package_lists) - 1, self.get_earliest_deadline)

        print(',,,,,sorteddd,,,,,,groups_pcks_with_similar_address')
        print(package_lists)
        
        self.assign_package_sets(package_lists, truck, time)
    
    
    def assign_pcks_with_distinct_addresses(self, truck, time):
        packages = self.hub.group_pcks_with_distinct_addresses()
        print("hub pck here ,,,,")
        print(self.hub.packages)
        print("truck pck here ,,,,")
        print(truck.packages)
        print(truck.isFull())
        
        i = 0
        while i < len(packages) and not truck.isFull() and not self.hub.isEmpty():
            package_id = packages[i]
            package = self.packageHashTable.lookup(package_id)
            if package is not None and package.status.is_ready(time):
                truck.add_single_package(package_id)
                self.hub.packages.remove(package_id)
                # change status to out for delivery
                package.status.add_to_history(State.EN_ROUTE, time)

            i += 1
        print("hub pck here ,, after,,,,")
        print(self.hub.packages)
        print("truck pck here ,,,,")
        print(truck.packages)
        print(truck.isFull())


    def load(self, truck, time):
        # Note: Can only be on truck n
        self.assign_constrained_packages(truck, time)

        ########### Assign packages to trucks (Must be delivered with #, #, ..)
        self.assign_grouped_packages(truck, time)
        
        #####
        self.assign_pcks_with_similar_address(truck, time)

        ######
        self.assign_pcks_with_distinct_addresses(truck, time)

        ####
        truck.status.addToHistory(State.EN_ROUTE, time)

        print(',,,truck.packages')
        for pck in truck.packages:
            print(self.packageHashTable.lookup(pck))

        print(',,,hubbbb')

        print(self.hub)

        print(',,,truck')

        print(truck)
       
