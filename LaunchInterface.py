from State import State
from ClockTime import ClockTime
from data.Constants import START_SHIFT, END_SHIFT
import re

def input_time():
    # Regex pattern for validating time in HH:MM AM/PM format (case insensitive)
    time_pattern = r'^(0[1-9]|1[0-2]):([0-5][0-9]) (am|pm)$'

    valid_input = False

    while not valid_input:
        t = input("\tEnter time HH:MM AM/PM: ").lower().strip()  # Convert input to lowercase

        # Check if input matches the pattern (case insensitive)
        if re.match(time_pattern, t):
            # Standardize AM/PM to uppercase
            t = t.upper()  # Convert the time to uppercase (e.g., "am" -> "AM", "pm" -> "PM")
            
            if ClockTime(t) >= START_SHIFT:
                valid_input = True
            else:
                print(f"\t>>> Shift starts at {START_SHIFT}")
        else:
            print("\t>>> Invalid time format. Please enter in HH:MM AM/PM format.")
    return t

def input_number(prompt):
    valid_input = False
    while not valid_input:
        user_input = input(prompt).strip()

        if user_input.isdigit():
            valid_input = True
        else:
            print(f"The input {user_input} is not a valid non-negative integer.")

    return user_input

def get_package_by_id(package_hash_table, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:  # Limit the number of attempts
        package_id = int(input_number('\tEnter package ID: '))
        package = package_hash_table.lookup(package_id)
        if package:
            return package  # Return the package if found
        attempts += 1  # Increment attempts if package is not found
    
    # If the maximum attempts are reached, return None
    print("Exceeded maximum attempts. Package not found.")
    return None

def get_truck_by_id(trucks, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:  # Limit the number of attempts
        truck_num = int(input_number(f"\tEnter Truck Number (1 through {len(trucks)}): "))
        if truck_num > 0 and truck_num <= len(trucks):
            return trucks[truck_num - 1]
        attempts += 1  # Increment attempts
    
    # If the maximum attempts are reached, return None
    print("Exceeded maximum attempts. Package not found.")
    return None

# Helper function to fetch address using address_id.
def fetch_address(address_id, package_hash_table):
    return package_hash_table.AddressHashTable.lookup(address_id) if address_id is not None else None

# Helper function to format address information.
def format_address(address): 
    if address:
        return (f"[Addr_id: {address.id} | {address.place} | {address.address}, "
                f"{address.city}, {address.state} {address.zip}]")
    return ""

def print_package_status_at_time(package, address, time):
    st = package.status.getStatusAt(time)
    print(f"Package ID: {package.id}-- status at {time}: {repr(st)}"\
        f"-- {'Delivered at' if st == State.DELIVERED else 'Expected to deliver at'}: {package.status.get_delivery_time()}"\
        f"-- Deadline: {package.deadline.get_time_str()}"\
        f"-- Truck No: {package.truck_id + 1}"
        f"-- Address: {format_address(address)}"
        )
        
    
def print_package_status_in_range(package, address, t1, t2):
    status_list_repr = ', '.join([f"{status[1]}: {repr(status[0])}" for status in package.status.get_status_in_range(t1, t2)])
    print(f"Package ID: {package.id}--- Status {t1}-{t2}: [{status_list_repr}]"\
            f"-- Deadline: {package.deadline.get_time_str()}"\
            f"-- Truck No: {package.truck_id + 1}"
            f"-- Address: {format_address(address)}"
            )


########### trucks status
def print_truck_status_at_time(package_hash_table, truck, time):
    status = truck.status.getStatusAt(time)  # Status format: (status, address_id, mileage, package_id, next_address_id, next_mileage)

    state = repr(status[0])
    address_id = status[1]
    mileage = status[2]
    package_id = status[3]
    next_address_id = status[4]
    next_mileage = status[5]

    # Fetch addresses
    address = fetch_address(address_id, package_hash_table)
    next_address = fetch_address(next_address_id, package_hash_table)
        
    # Build status string
    status_string = [f"\nStatus at {time}:\t{state}"]

    if package_id is not None and address is not None:
        status_string[0] += f" Package(s) with ID {address.packages}"

    status_string.append(f"Current Mileage:\t{round(mileage, 2)} miles")

    if address is not None:
        status_string.append(f"Last Visited Location:\t{format_address(address)}")

    if next_address is not None:
        status_string.append(
            f"Next Location:\t{format_address(next_address)}\n"
            f"Distance to the Next Location: {round(next_mileage - mileage, 2)} miles\n"
            f"Mileage at the Next Location: {round(next_mileage,2)} miles\n"
            f"Next Package(s) To Deliver: {"N/A" if len(next_address.packages) == 0 else next_address.packages}"
        )
    
    # Print the final result
    print("\n".join(status_string))


# Display overall status of all packages
def packages_overall_status(package_hash_table, hub):
    packages = package_hash_table.get_all_package_ids()
    packages.sort()

    print(f"\n============================= Overall status of all packages ===============================")
    for pck in packages:
        package = package_hash_table.lookup(pck)
        if package:
            address = fetch_address(package.address_id, package_hash_table)
            package_history_repr = ', '.join([f"{repr(status[0])}|{status[1]}" for status in package.status.trackingHistory])
            print(f"Package ID: {package.id}-- Tracking History=[{package_history_repr}]"
                f"-- Deadline: {package.deadline.get_time_str()}"\
                f"-- Delivered in Time: {'Yes' if package.status. is_delivered_by_time(package.deadline) else 'No'}"
                f"-- Truck No: {package.truck_id + 1}"
                f"-- Address: {format_address(address)}"
            )
    print(f"\t--------------------------------------------------------------------"
          f"\n\tEnd of Delivery Day: {hub.end_of_delivery_day}")


########### Drivers
def  drivers_overall_status(drivers):
     for driver in drivers:
        driver_assignments_repr = '\n\t'.join([f"{status[1]}: Drives truck No {status[0] + 1}" for status in driver.truck_assignments])
        print(f"\n------------------------------- Driver No: {driver.id + 1} --------------------------------------\n"
              f"Driver ID: {driver.id}\nHub: {driver.hub.name}\n"
              f"Truck Assignments:\n\t{driver_assignments_repr}")
              


#####
# Input a specific point in time t and Display overall status of all packages at t
def packages_status_at_time(package_hash_table):
    time = input_time()
      
    packages = package_hash_table.get_all_package_ids()
    packages.sort()

    print(f"\n=========================== Status of all packages at {time} ==============================\n"
              "Note:\tREADY = AT_THE_HUB and VALID_ADDRESS\n---------------------------------------")
    for pck in packages:
        package = package_hash_table.lookup(pck)
        if package:
            address = fetch_address(package.address_id, package_hash_table)
            print_package_status_at_time(package, address, time)
        
#
def specific_package_status_at_time(package_hash_table):
    package = get_package_by_id(package_hash_table)
    if package:
        address = fetch_address(package.address_id, package_hash_table)
        time = input_time()
        print(f"\n================== Status of the package with ID {package.id} at {time} ======================\n"
                "Note:\tREADY = AT_THE_HUB and VALID_ADDRESS\n---------------------------------------")
        print_package_status_at_time(package, address, time)
   

# Input two points in time t1 and t2, and display the status of all packages over the time range [t1, t2]
def packages_status_in_range(package_hash_table):
    print('From:')
    t1 = input_time()
    print('To:')
    t2 = input_time()
    
    packages = package_hash_table.get_all_package_ids()
    packages.sort()
    print(f"\n================== Status of all packages within the time range [{t1}, {t2}] ======================\n"
              "Note:\tREADY = AT_THE_HUB and VALID_ADDRESS\n---------------------------------------")
    for pck in packages:
        package = package_hash_table.lookup(pck)

        if package:
            address = fetch_address(package.address_id, package_hash_table)
            print_package_status_in_range(package, address, t1, t2)

        
def specific_package_status_in_range(package_hash_table):
    package = get_package_by_id(package_hash_table)
    if package:
        print('From:')
        t1 = input_time()
        print('To:')
        t2 = input_time()
        
        address = fetch_address(package.address_id, package_hash_table)

    print(f"\n============== Status of the package with ID {package.id} within the time range [{t1}, {t2}] =====================\n"    
              "Note:\tREADY = AT_THE_HUB and VALID_ADDRESS\n---------------------------------------")
    print_package_status_in_range(package, address, t1, t2)

    
# Input a package id and display details of the specific package
def specific_package_details(package_hash_table):
    package = get_package_by_id(package_hash_table)

    if package:
        address = package_hash_table.AddressHashTable.lookup(package.address_id)
        package_history_repr = '\n\t\t'.join([f"{status[1]}: {repr(status[0])}" for status in package.status.trackingHistory])
        requirements= ''
        if len(package.delivered_with) != 0:
            requirements += f"\n\t\t* Must be delivered with packages: {package.delivered_with}"
        if package.status.is_delayed():
            requirements += f"\n\t\t* Delayed on flight ---will not arrive to depot until {package.status.arrived_at.get_time_str()}"
        if package.corrected_address_id != -1:
            corrected_address = package_hash_table.AddressHashTable.lookup(package.corrected_address_id)
            if corrected_address:
                requirements += f"\n\t\t* Address updated at {package.address_updated_at.get_time_str()}\n\t\t-- Corrected Address:\t{format_address(corrected_address)}"
        if package.truck_id_requirement != -1:
            requirements += f"\n\t\t* Can only be on truck {package.truck_id + 1}"
        # Print details
        print(f"\n================================== Package with ID {package.id} Details =================================="
            f"\n\tPackage ID: {package.id}"
            f"\n\tAddress:\t{format_address(address)}"
            f"\n\tWeight: {package.weight}"        
            f"\n\tRequirements: {f"{requirements}" if requirements  else 'None'}"
            f"\n\tTracking History:\n\t\t{package_history_repr}"
            f"\n\tDeadline: {package.deadline.get_time_str()} {'(EOD)' if package.deadline.get_time_str() == END_SHIFT else ''}"
            f"\n\tDelivered in Time: {'Yes' if package.status. is_delivered_by_time(package.deadline) else 'No'}"
            f"\n\tTruck No: {package.truck_id + 1}")

######## Trucks #####

### Input a specific point in time t and Display overall status of all packages at t
def trucks_status_at_time(package_hash_table, trucks):
    time = input_time()
    total_mileage = 0.0

    print(f"\n=========================== Status of all trucks at {time} ==============================\n")
    for truck in trucks:
        print(f"\n----- Truck No. {truck.id + 1} -----\n")
        print_truck_status_at_time(package_hash_table, truck, time)

        status = truck.status.getStatusAt(time)
        total_mileage += status[2]

    print(f"\n---------------------------------\nTotal Mileage at {time}: {round(total_mileage, 2)} miles\n")
    
############
def specific_truck_status_at_time(package_hash_table, trucks):
    truck = get_truck_by_id(trucks)
    if truck:
        time = input_time()
        print(
            f"\n================== Status of Truck No. {truck.id + 1} at {time} ======================\n"
            f"Truck ID: {truck.id}"
        )
        print_truck_status_at_time(package_hash_table, truck, time)
#####
def specific_truck_details(package_hash_table, trucks):
    truck = get_truck_by_id(trucks)
    if truck:
        #Truck info
        truck_info = (
            f"\n------------------------------- Truck No: {truck.id + 1} --------------------------------------\n"
            f"Truck ID: {truck.id}\nHub: {truck.hub.name}\n"
            f"Max Capacity: {truck.maxCapacity} packages\n"
            f"Average Speed: {truck.speed} mph\n"
            f"Total Mileage of This Truck: {truck.mileage} miles\nTotal Milage of All Trucks: {truck.hub.trucks_total_mileage()} miles\n"
        )

        tracking_history = ["Tracking History:"]

        for status in truck.status.trackingHistory:
            
            state = repr(status[0])
            timestamp = status[1]
            address_id = status[2]
            mileage = status[3]
            package_id = status[4]

            status_string = [f"\t{timestamp}: {state} "]

            
            if package_id is not None:
                status_string.append(f"Package with ID {package_id}")

            if address_id is not None:
                address = package_hash_table.AddressHashTable.lookup(address_id)
                status_string.append(f" --- Current Mileage: {round(mileage, 2)} mi --- Location: {format_address(address)}")

            # tracking_history.append(status_string)
            tracking_history.append("".join(status_string))

        # print(truck_info + "\n".join(status_str for status_str in tracking_history))
        print(truck_info + "\n".join(tracking_history))


## Display the totale mileage of all trucks
def trucks_total_mileage(hub, trucks):
    print(f"End of Delivery Day: {hub.end_of_delivery_day}\n")
    
    # Generate truck mileage details
    mileage_details = [
        f"Truck No. {truck.id + 1} Mileage: {round(truck.mileage, 2)} miles" for truck in trucks
    ]
    
    # Print all truck mileages
    print("\n".join(mileage_details))
    
    # Print total mileage
    print(f"----------------------------------\nTotal Mileage: {round(hub.trucks_total_mileage(), 2)} miles")


######################
#### Package menu
def package_menu(package_hash_table, hub):     
    menu_prompt = ("\n========================================== Package Menu ==========================================\n"
        "\t1. Overall status of all packages\n"
        "\t2. Status of all packages at a point in time\n"
        "\t3. Status of all packages within a time range\n"
        "\t4. Status of a specific package at a point in time\n"
        "\t5. Status of a specific package within a time range\n"
        "\t6. Full details of a specific package\n"
        "\t7. Return to the main menu\n")
    
    done = False 
    while not done: 
        command = input(menu_prompt).lower().strip()
        if command == '1':
            packages_overall_status(package_hash_table, hub)
        elif command == '2':
            packages_status_at_time(package_hash_table)
        elif command == '3':
            packages_status_in_range(package_hash_table)
        elif command == '4':
            specific_package_status_at_time(package_hash_table)
        elif command == '5':
            specific_package_status_in_range(package_hash_table)
        elif command == '6':
            specific_package_details(package_hash_table)
        elif command == '7':
            done = True
        else: # Invalid input handling
            print("Invalid input, please enter a valid option (1 through 7).")

####
def truck_menu(package_hash_table, hub, trucks):
    menu_prompt = ("\n========================================== Truck Menu ==========================================\n"
            "\t1. Status of all trucks at a point in time\n"
            "\t2. Status of a specific truck at a point in time\n"
            "\t3. Full details of a specific truck\n"
            "\t4. Total Mileage of All Trucks\n"
            "\t5. Return to the main menu\n"
    )

    done = False
    while not done:
        command = input(menu_prompt).lower().strip()
        if command == '1':
            trucks_status_at_time(package_hash_table, trucks)
        elif command == '2':
            specific_truck_status_at_time(package_hash_table, trucks)
        elif command == '3':
            specific_truck_details(package_hash_table, trucks)
        elif command == '4':
            trucks_total_mileage(hub, trucks)
        elif command == '5':
            done = True
        else: # Invalid input handling
            print("Invalid input, please enter a valid option (1 through 5).")

####
def driver_menu(drivers):
    menu_prompt = ("\n========================================== Driver Menu ==========================================\n"
            "\t1. Overall Status of All Drivers\n"
            "\t2. Return to the main menu\n"
    )
    
    done = False
    while not done:
        command = input(menu_prompt).lower().strip()
        if command == '1':
            drivers_overall_status(drivers)
        elif command == '2':
            done = True
        else: # Invalid input handling
            print("Invalid input, please enter a valid option (1 through 2).")

############### Main Menu
def launch_interface(package_hash_table, hub, trucks, drivers):
    menu_prompt = ("\n=========================================== Main Menu ============================================\n"
                    "\t1. Package Menu\n"
                    "\t2. Truck Menu\n"
                    "\t3. Driver Menu\n"
                    "\t4. Quit\n")
    done = False 
    while not done:  # Exit when user enters '4'
        command = input(menu_prompt).lower().strip()
        if command == '1':
            package_menu(package_hash_table, hub)

        elif command == '2':
            truck_menu(package_hash_table, hub, trucks)

        elif command == '3':
            driver_menu(drivers)
            
        elif command == '4':
            done = True
        else: # Invalid input handling
            print("Invalid input, please enter a valid choice (1, 2, 3, or 4).")
