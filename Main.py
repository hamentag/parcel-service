from HashTableImp import HashTable
from Package import Package
from Truck import Truck
from HubClass import Hub
from ClockTime import ClockTime
from utils.CsvPackageLoader import read_packages_from_csv
from utils.CsvAddressLoader import readAddresses


hash_table = HashTable()

# Insert packages into the hash table
for package in read_packages_from_csv('csv/Package_File.csv'):
    hash_table.insert(package.id, package)

print("The Hash Table has been successfully populated.")


# Display the hash table
# print("Hash Table after insertion:")
# hash_table.display()


package_ids = hash_table.get_all_package_ids()
print("All package IDs:", package_ids)


# Create Truck objects
trucks = [Truck(i) for i in range(3)]

# Hub
hub = Hub()
hub.trucks.append(trucks[2])    #Truck 3 starts at the hub

#### Apply business constraints defined in project notes
for package_id in package_ids:
    package = hash_table.lookup(package_id)
    if package is not None:
        # Assign packages to trucks (Can only be on truck #)
        if package.truckId != -1:
            trucks[package.truckId].packages.append(package_id)
            
        ############print
        print(package.deliveredWith)

        deliveredWithSet = package.deliveredWith

        if len(deliveredWithSet) != 0:
            
            deliveredWithSet.add(package_id)
            groupedPackages = hash_table.grouped

            if groupedPackages:  # There are already some grouped packages
                found_group = False
                for group in groupedPackages:
                    if group & deliveredWithSet:  # intersection
                        group.update(deliveredWithSet)  # Merge
                        found_group = True
                        break

                if not found_group:
                    groupedPackages.append(deliveredWithSet)   
            else:
                groupedPackages.append(deliveredWithSet)
                print(groupedPackages)



########### Assign packages to trucks (Must be delivered with #, #, ..)
########## print
print(hash_table.grouped)

# All the group members assigned to truck 1 or truck 2
# Note: All grouped packages are available at 08:00 AM
for group in hash_table.grouped:
    if trucks[0].isNotFullAfterAdding(len(group)):
        trucks[0].packages.extend(group)
    elif trucks[1].isNotFullAfterAdding(len(group)):
        trucks[1].packages.extend(group)
    else:
        break

def isPackageAvailableAt(package_id, thisTime):
    package = hash_table.lookup(package_id)
    if package is not None:
        return package.isAvailableAt(thisTime)
    return False

 
start = ClockTime("08:00 AM")
### Assign packages to trucks (availabe pck at 08:00 AM)
for package_id in package_ids:
    if package_id in trucks[0].packages or package_id in trucks[1].packages:
        continue
    if not isPackageAvailableAt(package_id, start):
        hub.packages.append(package_id)
        continue
    if trucks[0].isNotFull():
        trucks[0].packages.append(package_id)
    elif trucks[1].isNotFull():
        trucks[1].packages.append(package_id)
    elif package_id not in hub.packages:
        hub.packages.append(package_id)




def setOutForDeliveryAt(package_id, thisTime):
    package = hash_table.lookup(package_id)
    if package is not None:
        package.outForDeliveryAt = thisTime
# Set status out for delivery (trucks 1 and 2 packages)
for package_id in trucks[0].packages:
    setOutForDeliveryAt(package_id, start)


########## print
# Display the hash table
print("Hash Table:")
hash_table.display()

for j in range(3):
    print(trucks[j])


print(hub)

