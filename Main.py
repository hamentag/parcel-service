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
from State import State
from utils.PackageDataLoader import lod_packages_data
from utils.AddressDataLoader import load_addresses_data

from LoadingPackages import loading_packages
from ExecutingDelivery import executing_delivery
from LaunchInterface import launch_interface

from data.Constants import START_SHIFT, NUM_DRIVERS ,NUM_TRUCKS 


################### Create instances of hash tables and distance map ######################
address_hash_table = AddressHashTable()
package_hash_table = PackageHashTable(address_hash_table)

########################## Load data #############################################
lod_packages_data(package_hash_table)
load_addresses_data(address_hash_table)
package_hash_table.collect_packages()
###############



# Create Hub, Truck snd Driver objects
hub = Hub("Western Governors University", package_hash_table)
trucks = [Truck(i, hub) for i in range(NUM_TRUCKS)]
drivers = [Driver(i, hub) for i in range(NUM_DRIVERS)]


time = ClockTime()
# 
loading_sequences = [START_SHIFT] * min(NUM_TRUCKS, NUM_DRIVERS)

print("Starting to load and deliver packages...")
done = False
i = 0
while not done:
   
    time.set_time_to_min_of(loading_sequences)

    selected_truck = hub.selectTruckWithMinMileage(time)

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

print(
    f"All packages have been successfully loaded and delivered!\n"
    f"End of Delivery Day: {hub.end_of_delivery_day}\n"
    f"Num. of packages delivered at {hub.end_of_delivery_day}: {package_hash_table.get_num_delivered_pcks(hub.end_of_delivery_day)} packages"
)

########################################
# Launch user interface
launch_interface(package_hash_table, hub, trucks, drivers)
