from hashTables.HashTable import HashTable

class PackageHashTable(HashTable):
    def __init__(self):
        super().__init__()



    #
    def getAllPackageIds(self):
        return super().getAllElementIds() 

    ###
    # Method to return grouped packages
    def getGgroupedPackages(self):
        groupedPackages = []
        for entry in self.table:
            for p in entry:
                deliveredWith = p.deliveredWith

                if len(deliveredWith) != 0:
                    
                    deliveredWith.add(p.id)

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
                        print(groupedPackages)
        return groupedPackages


    # Group packages by their addressId
    def group_by_address_id(self):
        address_groups = {}

        # Iterate over all packages in the hash table
        for entry in self.table:
            for p in entry:
                addressId = p.addressId
                if addressId not in address_groups:
                    address_groups[addressId] = []
                address_groups[addressId].append(p.id)

        return [group for group in address_groups.values() if len(group) >= 2]

  