class Hub:
    HUB_ADDRESS_ID = 0
    def __init__(self, name, package_hash_table, address_id=HUB_ADDRESS_ID):
        self.name = name
        self.address_id = address_id
        self.package_hash_table = package_hash_table
        self.trucks = []
        self.packages = []

        self.packages = self.package_hash_table.getAllPackageIds()

        # for package_id in self.package_hash_table.getAllPackageIds():
        #     self.packages.append(package_id)
        
        
    def selectTruckWithMinMileage(self):
        minTruck = self.trucks[0]
        for truck in self.trucks:
            if truck.mileage < minTruck.mileage:
                minTruck = truck
        return minTruck

    def isEmpty(self):
        return len(self.packages) == 0
    
    # Method to return grouped packages
    def get_grouped_packages(self):
        groupedPackages = []
        for p_id in self.packages:
            package = self.package_hash_table.lookup(p_id)
            if package is not None:
                deliveredWith = package.deliveredWith

                if len(deliveredWith) != 0:
                    
                    deliveredWith.add(p_id)

                    if groupedPackages:  # There are already some grouped packages
                        found = False
                        for group in groupedPackages:
                            if group & deliveredWith:  # intersection
                                group.update(deliveredWith)  # Merge
                                found = True
                                break

                        if not found:
                            groupedPackages.append(deliveredWith)
                    else:
                        groupedPackages.append(deliveredWith)
            
        return groupedPackages
    
     
    def group_by_address_id(self):
        address_groups = {}

        for p_id in self.packages:
            package = self.package_hash_table.lookup(p_id)
            if package is not None:
                addressId = package.addressId
                if addressId not in address_groups:
                    address_groups[addressId] = set()
                address_groups[addressId].add(p_id)

        return address_groups
    
    ############ adddress
    def groups_pcks_with_similar_address(self):
        address_groups = self.group_by_address_id()
        return [group for group in address_groups.values() if len(group) >= 2]
    
    # def groups_single_pck_in_address(self, package_hash_table):
    #     address_groups = self.group_by_address_id(package_hash_table)
    #     return [group for group in address_groups.values() if len(group) == 1]   
    
    def group_pcks_with_distinct_addresses(self):
        address_groups = self.group_by_address_id()
        result = []
        for group in address_groups.values():
            if len(group) == 1:
                # result.append(group[0])
                result.extend(group)
        return result


    # # Group packages by their addressId
    # def group_bbbbby_address_id(self, package_hash_table):
    #     address_groups = {}

    #     for p_id in self.packages:
    #         package = package_hash_table.lookup(p_id)
    #         if package is not None:                
    #             addressId = package.addressId
    #             if addressId not in address_groups:
    #                 address_groups[addressId] = []
    #             address_groups[addressId].append(p_id)
            

    #     return [group for group in address_groups.values() if len(group) >= 2]

    # def get_distinct_deadlines(self):
    #     deadlines = {}
    #     for p_id in self.packages:
    #         package = self.package_hash_table.lookup(p_id)
    #         if package is not None:
    #             deadline = package.deadline
    #             deadlines.add(deadline)
    #     return deadlines

    def trucks_total_mileage(self):
        total = 0
        for truck in self.trucks:
            total += truck.mileage
        return total

    def __repr__(self):
        trucks_repr = ', '.join([repr(truck) for truck in self.trucks])
        packages_repr = ', '.join([repr(package) for package in self.packages])
        return f"Hub(name={self.name}, address_id={self.address_id}, trucks=[{trucks_repr}], packages=[{packages_repr}])"
