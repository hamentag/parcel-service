from hashTables.PackageHashTable import PackageHashTable
# from HashTable import HashTable
from hashTables.AddressHashTable import AddressHashTable
from Package import Package
from Truck import Truck
from HubClass import Hub
from ClockTime import ClockTime
from utils.CsvPackageLoader import read_packages_from_csv
from utils.CsvAddressLoader import readAddresses


# packageHashTable = HashTable()
packageHashTable = PackageHashTable()  

# Insert packages into the hash table
for package in read_packages_from_csv('csv/Package_File.csv'):
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
print(packageHashTable.getGgroupePackages())

# All the group members assigned to truck 1 or truck 2
# Note: All grouped packages are available at 08:00 AM
for group in packageHashTable.getGgroupePackages():
    if trucks[0].isNotFullAfterAdding(len(group)):
        trucks[0].packages.extend(group)
    elif trucks[1].isNotFullAfterAdding(len(group)):
        trucks[1].packages.extend(group)
    else:
        break

# Start
start = ClockTime("08:00 AM")

def setOutForDeliveryAt(package_id, thisTime):
    package = packageHashTable.lookup(package_id)
    if package is not None:
        package.outForDeliveryAt = thisTime
# Set status out for delivery (trucks 1 and 2 packages)
for package_id in trucks[0].packages:
    setOutForDeliveryAt(package_id, start)


########## print
# Display the hash table
print("Hash Table:")
packageHashTable.display()

for j in range(3):
    print(trucks[j])


print(hub)


# ###################### Addresses #########################
addressHashTable = AddressHashTable()
# Insert addresses into the hash table
for address in readAddresses('csv/Address_File.csv'):
    addressHashTable.insert(address.id, address)


# Display the hash table / addresses
print("Hash Table (addressess) after insertion:")
addressHashTable.display()


# print(addressHashTable.grouped)

# #########################################################


print (trucks[0])
print (trucks[1])
print(hub)


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

print (trucks[0])
print (trucks[1])
print(hub)



def isPackageAvailableAt(package_id, thisTime):
    package = packageHashTable.lookup(package_id)
    if package is not None:
        return package.isAvailableAt(thisTime)
    return False

 
# start = ClockTime("08:00 AM")
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

print ("final,,")
print (trucks[0])
print (trucks[1])
print(hub)
