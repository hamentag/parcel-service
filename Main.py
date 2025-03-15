# Student ID: 011800245
# Hamza Amentag
# Data Structures and Algorithms II — C950
# NHP3 Task 2: WGUPS Routing Program Implementation
#######################################################################################
from data_structures.PackageHashTable import PackageHashTable
from data_structures.AddressHashTable import AddressHashTable

from Truck import Truck
from Driver import Driver
from Hub import Hub
from ClockTime import ClockTime
from utils.PackageDataLoader import lod_packages_data
from utils.AddressDataLoader import load_addresses_data

from LoadingPackages import loading_packages
from ExecutingDelivery import executing_delivery

from data.Constants import START_SHIFT, NUM_DRIVERS ,NUM_TRUCKS 


################### Create instances of hash tables and distance map ######################
address_hash_table = AddressHashTable()
package_hash_table = PackageHashTable(address_hash_table)

########################## Load data #############################################
lod_packages_data(package_hash_table)
load_addresses_data(address_hash_table)

###############





# Create Hub, Truck snd Driver objects
hub = Hub("Western Governors University", package_hash_table)
trucks = [Truck(i, hub) for i in range(NUM_TRUCKS)]
drivers = [Driver(i, hub) for i in range(NUM_DRIVERS)]


time = ClockTime()
# 
loading_sequences = [START_SHIFT] * min(NUM_TRUCKS, NUM_DRIVERS)


done = False
i = 0
while not done:
   
    # time = ClockTime(loading_sequences.pop(0))
    # loading_sequences.pop(min_value)
    time.set_time_to_min_of(loading_sequences)

    selected_truck = hub.selectTruckWithMinMileage()

    selected_driver = drivers[i % NUM_DRIVERS]



    loading_packages(package_hash_table, selected_truck, selected_driver, time)

    #Executing Delivery
    executing_delivery(package_hash_table, hub, selected_truck, time)
    

    loading_sequences.append(time.get_time_str())
    # sort(loading_sequences, 0, len(loading_sequences) - 1, lambda var: ClockTime(var))      #min

    
    i += 1
    if not package_hash_table.has_ready_pcks(time):
        done = True
# End While


# The delivery day ends
hub.end_of_delivery_day = max(loading_sequences)









print('loading_sequences end,,,')
print(loading_sequences)

package_hash_table.display()
for pck in package_hash_table.getAllPackageIds():
    p = package_hash_table.lookup(pck)
    print(f"deadline: {p.deadline} --- status at 08:33 am: {p.status.getStatusAt(ClockTime('08:33 AM'))} --- status at deadline: {p.status.getStatusAt(p.deadline)}")


def get_deadline(package_id):
            package = package_hash_table.lookup(package_id)
            if package is not None:
                return package.deadline
def get_delv_time(package_id):
            package = package_hash_table.lookup(package_id)
            if package is not None:
                return package.status.get_delivery_time()
            
pcks = package_hash_table.getAllPackageIds()
# sort(pcks, 0, len(pcks) - 1, get_deadline)
# sort(pcks, 0, len(pcks) - 1, get_delv_time) #################
for pck in pcks:
    p = package_hash_table.lookup(pck)
    print(f"pck_id: {p.id} --- deadline: {p.deadline} --- Delivered at: {p.status.get_delivery_time()} --- address_id = {p.address_id} --- status at deadline: {p.status.getStatusAt(p.deadline)} --- truck_id = {p.truck_id} --- readt at: {p.status.get_ready_time()}")
print("each truck id...")

for pck in pcks:
    p = package_hash_table.lookup(pck)
    print(f"pck_id: {p.id} --- deadline: {p.deadline} --- Delivered at: {p.status.get_delivery_time()}  --- status at deadline: {p.status.getStatusAt(p.deadline)} --- truck_id = {p.truck_id} --- readt at: {p.status.get_ready_time()} --- En route at: {p.status.get_en_route_time()}")

for pck in pcks:
      if pck == 9:
        print(f"pck 9 ,,, addr_id = {package_hash_table.lookup(pck).get_address_id(time)}")
for index, truck in enumerate(trucks):
    print(f"mileage of truck index {index} is {round(truck.mileage, 2)} miles")

print(f"total_mileage: {round(hub.trucks_total_mileage(), 2)} miles")



# print( 'num of deliv at 11:25 AM')
# print(package_hash_table.get_num_delivered_pcks(ClockTime('11:25 AM')))
# for t in trucks:
#       print(t)
#       print("spa        ce")

# print(hub)