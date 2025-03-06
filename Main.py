#######################################################################################
from data_structures.PackageHashTable import PackageHashTable
from data_structures.AddressHashTable import AddressHashTable
from data_structures.DistanceMap import DistanceMap
from Package import Package
from Loader import Loader
from DeliveryProcess import DeliveryProcess
from Truck import Truck
from Driver import Driver
from HubClass import Hub
from ClockTime import ClockTime
from State import State
from utils.CsvPackageLoader import lod_packages_data
from utils.CsvAddressLoader import load_addresses_data
from utils.CsvDistanceLoader import load_distance_data
from utils.Quicksorter import sort

START_SHIFT = '08:00 AM'
NUM_DRIVERS = 2
NUM_TRUCKS = 3


################### Create instances of hash tables and distance map ######################
package_hash_table = PackageHashTable()
address_hash_table = AddressHashTable()
distance_map = DistanceMap()

########################## Read data #############################################
lod_packages_data('data/Package_File.csv', package_hash_table)
load_addresses_data('data/Address_File.csv', address_hash_table)
load_distance_data('data/Distance_File.csv', distance_map)



# Create Hub, Truck snd Driver objects
hub = Hub("Western Governors University", package_hash_table)
trucks = [Truck(i, hub) for i in range(NUM_TRUCKS)]
drivers = [Driver(i, hub) for i in range(NUM_DRIVERS)]


# 
loading_sequences = [START_SHIFT] * min(NUM_TRUCKS, NUM_DRIVERS)


loader = Loader(package_hash_table, hub)
delivery_process = DeliveryProcess(package_hash_table, distance_map, hub)

i = 0
while not hub.isEmpty():
   
    time = ClockTime(loading_sequences.pop(0))

    selected_truck = hub.selectTruckWithMinMileage()

    selected_driver = drivers[i % NUM_DRIVERS]



    loader.load(selected_truck, selected_driver, time)

    delivery_process.execute(selected_truck, time)

    print("time after del prcc,,")
    print(time)


    loading_sequences.append(time.get_time_str())
    sort(loading_sequences, 0, len(loading_sequences) - 1, lambda var: ClockTime(var))


    print('loading_sequences')
    print(loading_sequences)

    
    i += 1
# End While







print('loading_sequences end,,,')
print(loading_sequences)

package_hash_table.display()
for pck in package_hash_table.getAllPackageIds():
    p = package_hash_table.lookup(pck)
    print(f"deadline: {p.deadline} --- status at deadline: {p.status.getStatusAt(ClockTime('08:33 AM'))} --- status at deadline: {p.status.getStatusAt(p.deadline)}")

for pck in package_hash_table.getAllPackageIds():
    p = package_hash_table.lookup(pck)
    print(f"deadline: {p.deadline} --- Delivered at: {p.status.get_delivery_time()} --- status at deadline: {p.status.getStatusAt(p.deadline)}")


for index, truck in enumerate(trucks):
    print(f"mileage of truck index {index} is {truck.mileage} miles")

print(f"total_mileage: {hub.trucks_total_mileage()} miles")


print("truck indx 0")
print(trucks[0])
print(trucks[0].status.getStatusAt(ClockTime('10:56 AM')))


print("hub:")
print(hub)

print("driversss:")
for dr in drivers:
    print(dr)