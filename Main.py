from hashTables.PackageHashTable import PackageHashTable
# from HashTable import HashTable
from hashTables.AddressHashTable import AddressHashTable
from Package import Package
from Truck import Truck
from HubClass import Hub
from ClockTime import ClockTime
from State import State
from utils.CsvPackageLoader import readPackagesData
from utils.CsvAddressLoader import readAddressesData
from utils.CsvDistanceLoader import readDistanceData
from utils.QuicksortFunction import quicksort


# packageHashTable = HashTable()
packageHashTable = PackageHashTable()  

# Insert packages into the hash table
for package in readPackagesData('data/Package_File.csv'):
    packageHashTable.insert(package.id, package)

print("The Hash Table has been successfully populated.")

####### del data ? # del packagesFrom Csv file


package_ids = packageHashTable.getAllPackageIds()
print("All package IDs:", package_ids)


# Create Truck objects
trucks = [Truck(i) for i in range(3)]

# Hub
hub = Hub()
hub.trucks.append(trucks[2])    #Truck 3 starts at the hub

#### Apply business requirements defined in project notes
for package_id in package_ids:
    package = packageHashTable.lookup(package_id)
    if package is not None:
        # Assign packages to trucks (Can only be on truck #)  encapsulate?
        if package.truckId != -1:
            trucks[package.truckId].packages.append(package_id)
            


########### Assign packages to trucks (Must be delivered with #, #, ..)
########## print
print(packageHashTable.getGgroupedPackages())

# All the group members assigned to truck 1 or truck 2
# Note: All grouped packages are available at 08:00 AM
for group in packageHashTable.getGgroupedPackages():
    if trucks[0].isNotFullAfterAdding(len(group)):
        trucks[0].packages.extend(group)
    elif trucks[1].isNotFullAfterAdding(len(group)):
        trucks[1].packages.extend(group)
    else:
        break





# ###################### Addresses #########################
addressHashTable = AddressHashTable()
# Insert addresses into the hash table
for address in readAddressesData('data/Address_File.csv'):
    addressHashTable.insert(address.id, address)


# Display the hash table / addresses
print("Hash Table (addressess) after insertion:")
addressHashTable.display()

#####################


def selectTruckWithMostPackagesAtAddress(group):
    truck1Count = 0
    truck2Count = 0
    for pck in trucks[0].packages:
        if pck in group:
            truck1Count += 1
    for pck in trucks[1].packages:
        if pck in group:
            truck2Count += 1
    return (-1, truck1Count) if truck1Count == truck2Count else ((0, truck1Count) if truck1Count > truck2Count else (1, truck2Count))


groupedPackagesByAddress = packageHashTable.group_by_address_id()

print("tst grouped by address,.,,,")
# Display the grouped packages (ids)
for group in groupedPackagesByAddress:
    index = selectTruckWithMostPackagesAtAddress(group)
    print(index)
    if index[0] != -1:
        # trucks[index[0]].packages.extend(group)
        trucks[index[0]].packages = list(set(trucks[index[0]].packages) | set(group))





def isPackageAvailableAt(package_id, thisTime):
    package = packageHashTable.lookup(package_id)
    if package is not None:
        return package.status.isAvailableAt(thisTime)
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


# Start
# start = ClockTime("08:00 AM")

def setOutForDeliveryAt(package_id, thisTime):          #Package class method?
    package = packageHashTable.lookup(package_id)
    if package is not None:
        # package.outForDeliveryAt = thisTime
        package.status.addToHistory(State.OUT_FOR_DELIVERY, thisTime)
# Set status out for delivery (trucks 1 and 2 packages)
for package_id in trucks[0].packages:
    setOutForDeliveryAt(package_id, start)
for package_id in trucks[1].packages:
    setOutForDeliveryAt(package_id, start)


########### print ################
print("tstt,,,1,,:")
for pi in trucks[0].packages:
    package = packageHashTable.lookup(pi)
    if package is not None:
        print(package)
print("tstt,,,2,,:")
for pi in trucks[1].packages:
    package = packageHashTable.lookup(pi)
    if package is not None:
        print(package)




################ distance

distance_hash_table = readDistanceData('data/Distance_File.csv')

print("all dist,,,")
print(distance_hash_table.get_all_distances(0))


dists = distance_hash_table.get_sorted_distances(0, [1,2,3,4,5])
dists2 = distance_hash_table.get_sorted_distances(0, {1,2,3,4,5})

print("list,,,")
print(dists)
print("set,,,")
print(dists2)
# Sort the distances using quicksort
# quicksort(dists, 0, len(dists) - 1)

# print(dists)


# # Sort the distances using quicksort
# quicksort(distances, 0, len(distances) - 1)



########## print
# print("Hash Table:")
# packageHashTable.display()

# for j in range(3):
#     print(trucks[j])


# print(hub)

