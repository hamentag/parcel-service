# Student ID: 011800245
# Hamza Amentag
# Data Structures and Algorithms II — C950
# NHP3 Task 2: WGUPS Routing Program Implementation
###############################################################
## For Time and Space Complexity:
# n: The number of packages.
# m: The number of addresses.

###############################################################
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


## Create instances of package and address hash tables
address_hash_table = AddressHashTable()     # Instantiate the AddressHashTable to store address-related data
package_hash_table = PackageHashTable(address_hash_table) # Instantiate PackageHashTable, which uses the AddressHashTable for address-related operations

# Load the package data from the csv file
# Time Complexity: O(n), Space Complexity: O(n)
lod_packages_data(package_hash_table)    # Load package data into the package hash table

# Load the address data from the csv file
# Time Complexity: O(m), Space Complexity: O(m)
load_addresses_data(address_hash_table)  # Load address data into the address hash table

## # Collect all the packages that must be delivered together
package_hash_table.collect_packages()    

############################################################################################ 
# Create Hub, Truck, Driver, and time objects
hub = Hub("Western Governors University", package_hash_table) # Instantiate the hub (Starting location for deliveries)
trucks = [Truck(i, hub) for i in range(NUM_TRUCKS)]       # Create a list of trucks; each truck is assigned an ID and the hub
drivers = [Driver(i, hub) for i in range(NUM_DRIVERS)]    # Create a list of drivers, each assigned an ID and the hub
time = ClockTime()       # Create a clock object to manage the time during the deliveries

# Initialize loading sequences with the start shift time
# loading_sequences is a list of points in time at which a pair truck-driver is ready to start loading packages
loading_sequences = [START_SHIFT] * min(NUM_TRUCKS, NUM_DRIVERS)

print("Starting to load and deliver packages...")
done = False
i = 0

# Time complexity O(n): The while loop runs as long as there are packages to be delivered
# Space Complexity: O(1).
# >>> For the entire main function:
    # Total time complexity of O(n^2)
    # Total Space complexity of O(n)
while not done:

    # Set the current time to the minimum of the loading sequences
    # Time Complexity: O(1), Space Complexity: O(1)
    time.set_time_to_min_of(loading_sequences)

    # Select the truck with the minimum mileage from the hub
    # Time Complexity: O(t). where t is the number of truks. Since t is a constant much smaller 
    # than n (number of packages), overall time complexity is O(1)
    # Space Complexity: O(t), and it is also treated as O(1) relative to n
    selected_truck = hub.selectTruckWithMinMileage(time)

    # Select the driver for this delivery based on the round-robin approach 
    # (drivers are selected in a cyclic order with no preference)
    selected_driver = drivers[i % NUM_DRIVERS]      # Assign drivers in a cyclic way

    # Load packages onto the selected truck for the selected driver at the current time
     # Time Complexity: O(n). Space Complexity: O(1). 
    loading_packages(package_hash_table, selected_truck, selected_driver, time)

    # Execute the delivery of the loaded packages
    # Time Complexity: O(m). Space Complexity: O(1).
    executing_delivery(package_hash_table, hub, selected_truck, time)
    
    # Record the time of the current loading event for the loading sequence
    loading_sequences.append(time.get_time_str()) 

    i += 1

    # Check if there are any packages ready to be delivered
    if not package_hash_table.has_ready_pcks(time):
        done = True     # Stop the loop when no more packages are ready
        
# End of while loop

# Mark the end of the delivery day
hub.end_of_delivery_day = max(loading_sequences)

# Output summary of the delivery status
print(
    f"All packages have been successfully loaded and delivered!\n"
    f"End of Delivery Day: {hub.end_of_delivery_day}\n"
    f"Num. of packages delivered at {hub.end_of_delivery_day}: {package_hash_table.get_num_delivered_pcks(hub.end_of_delivery_day)} packages"
)

## Launch user interface for interacting with the system
launch_interface(package_hash_table, hub, trucks, drivers)
