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
from utils.Quicksorter import sort


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



loading_sequences = [start.get_time_str(), start.get_time_str()]

ld = [start.get_time_str(), start.get_time_str()]

NUM_DRIVERS = 2

# load.pop(0)
# load.apend(t)


loader = Loader(packageHashTable, hub)
delivery_process = DeliveryProcess(packageHashTable, distance_hash_table, hub)

i = 0
while len(hub.packages) > 0:
   
    time = ClockTime(loading_sequences.pop(0))

    selectedTruck = hub.selectTruckWithMinMileage()
    
    

    # Note: Can only be on truck #
    # loader.assign_constrained_packages(selectedTruck)

    print('selectedTruck')
    print(selectedTruck)

    loader.load(selectedTruck, time)

    delivery_process.execute(selectedTruck, time)



  

    print("selectedTruck ...??")
    print(selectedTruck)
    print("selectedTruck.status.getStatusAt('09:25 AM')")
    print(selectedTruck.status.getStatusAt('09:25 AM'))


    print("time after del prcc,,")
    print(time)

    loading_sequences.append(time.get_time_str())
    sort(loading_sequences, 0, len(loading_sequences) - 1, lambda var: ClockTime(var))

    
    # def get_val(var):
    #     return ClockTime(var)    

    ld.append(time.get_time_str())
    sort(ld, 0, len(ld) - 1, lambda var: ClockTime(var)) 

    


    print('loading_sequences')
    print(loading_sequences)

    


    i += 1

    print("i = ")
    print(i)
    print("i % NUM_DRIVERS= ")
    print(i % NUM_DRIVERS)

# stp


print(",,,ld = ")
print(ld)


print('loading_sequences end,,,')
print(loading_sequences)

packageHashTable.display()
for pck in packageHashTable.getAllPackageIds():
    p = packageHashTable.lookup(pck)
    print(f"deadline: {p.deadline} --- status at deadline: {p.status.getStatusAt(ClockTime('08:33 AM'))} --- status at deadline: {p.status.getStatusAt(p.deadline)}")

for pck in packageHashTable.getAllPackageIds():
    p = packageHashTable.lookup(pck)
    print(f"deadline: {p.deadline} --- Delivered at: {p.status.get_delivery_time()} --- status at deadline: {p.status.getStatusAt(p.deadline)}")


for index, truck in enumerate(trucks):
    print(f"mileage of truck index {index} is {truck.mileage} miles")

print(f"total_mileage: {hub.trucks_total_mileage()} miles")
