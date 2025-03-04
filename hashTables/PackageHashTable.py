from hashTables.HashTable import HashTable

class PackageHashTable(HashTable):
    def __init__(self):
        super().__init__()



    #
    def getAllPackageIds(self):
        return super().getAllElementIds() 

    ###
    # Method to return grouped packages
    def getGroupedPackages(self):
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
                        # print(groupedPackages)
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
    

    # ## (pck_id, deadline)
    # def to_24hr_format(time_str):
    #     if deadline_str == "EOD":
    #         deadline_str = "11:59 PM"
    
    #     deadline_str_24hr = to_24hr_format(deadline_str)

    #     time_part, period = time_str.split()
    #     hour, minute = map(int, time_part.split(':'))
        
    #     if period == "AM":
    #         if hour == 12:
    #             hour = 0  # Midnight case (12:xx AM becomes 00:xx)
    #     else:  # PM
    #         if hour != 12:
    #             hour += 12  # PM times (except 12 PM) should be converted to 24-hour format
        
    #     return f"{hour:02}:{minute:02}"

  