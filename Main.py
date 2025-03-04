from hashTables.PackageHashTable import PackageHashTable
# from HashTable import HashTable
from hashTables.AddressHashTable import AddressHashTable
from Package import Package
from Loader import Loader
from DeliveryProcess import DeliveryProcess
from Truck import Truck
from HubClass import Hub
from ClockTime import ClockTime
from State import State
from utils.CsvPackageLoader import readPackagesData
from utils.CsvAddressLoader import readAddressesData
from utils.CsvDistanceLoader import readDistanceData
from utils.QuicksortFunction import quicksort


################################################## packageHashTable #############################################
packageHashTable = PackageHashTable()  

# Insert packages into the hash table
for package in readPackagesData('data/Package_File.csv'):
    packageHashTable.insert(package.id, package)

print("The Hash Table has been successfully populated.")



# ################################################## Addresses ###################################################
addressHashTable = AddressHashTable()
# Insert addresses into the hash table
for address in readAddressesData('data/Address_File.csv'):
    addressHashTable.insert(address.id, address)


# Display the hash table / addresses
print("Hash Table (addressess) after insertion:")
addressHashTable.display()



#################################################### distances #####################################################
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

####################################################################################################################


###########
package_ids = packageHashTable.getAllPackageIds()
print("All package IDs:", package_ids)


# Hub
hub = Hub("Western Governors University", packageHashTable)

# Create Truck objects
trucks = [Truck(i, hub) for i in range(3)]



start = ClockTime("08:00 AM")

for truck in trucks:
    hub.trucks.append(truck)
    truck.status.addToHistory(State.AT_THE_HUB, start)

for package_id in package_ids:
    hub.packages.append(package_id)



load = []
load.append(start)
load.append(start)
# load.pop(0)
# load.apend(t)


loader = Loader(packageHashTable, hub)
delivery_process = DeliveryProcess(packageHashTable, distance_hash_table, hub)

while len(hub.packages) > 0:
   
    time = load.pop(0)

    selectedTruck = hub.selectTruckWithMinMileage()
    
    

    # Note: Can only be on truck #
    # loader.assign_constrained_packages(selectedTruck)

    print('selectedTruck')
    print(selectedTruck)

    loader.load(selectedTruck, time)

    delivery_process.fct(selectedTruck, time)





