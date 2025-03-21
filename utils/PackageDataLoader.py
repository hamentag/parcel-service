import csv
from Package import Package
from ClockTime import ClockTime
from PackageStatus import PackageStatus
from data.Constants import PACKAGE_FILE_PATH, START_SHIFT, END_SHIFT

# Read package data from CSV file and return a list of Package objects.
def read_package_csv_file():
    packages = []
    with open(PACKAGE_FILE_PATH, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Skip empty rows
                id = int(row[0])                
                address_id = int(row[1])

                # EOD = 11:59 PM
                deadline = ClockTime(END_SHIFT if row[2] == "EOD" else row[2])

                weight = row[3]
                
                truck_id_requirement =  int(row[4]) if  row[4] != '' else -1   # truck_id = 0, 1, or 2

                arrived_at = ClockTime(START_SHIFT if row[5] == '' else row[5])

                corrected_address_id = int(row[6]) if  row[6] != '' else -1

                address_updated_at = ClockTime(START_SHIFT if row[7] == '' else row[7])

                delivered_with = {int(item) for item in row[8].split(';') if item.isdigit()}

                status = PackageStatus(deadline, arrived_at, address_updated_at)

                # Create a Package object using the extracted data
                package = Package(id, address_id, deadline, weight, corrected_address_id, address_updated_at, truck_id_requirement, delivered_with, status)
                packages.append(package)
    return packages


def lod_packages_data(package_hash_table):
    print("Starting to populate the hash table...")
    # Insert packages into the hash table
    for package in read_package_csv_file():
        package_hash_table.insert(package.id, package)
    print("The Hash Table has been successfully populated.")
