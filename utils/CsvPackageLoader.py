import csv
from Package import Package
from ClockTime import ClockTime

# Read package data from CSV file and return a list of Package objects.
def read_packages_from_csv(file_path):
    packages = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Skip empty rows
                id = int(row[0])                
                addressId = row[1]
                address = row[2]
                city = row[3]
                state = row[4]
                zip_code = row[5]

                print(row[6])

                # EOD = 11:59 PM
                deadline = ClockTime("11:59 PM" if row[6] == "EOD" else row[6])

                weight = row[7]
                
                truckId = int(row[8]) if  row[8] != '' else -1   # truckId = 0, 1, or 2

                arrivedAt = ClockTime("08:00 AM" if row[9] == '' else row[9])


                isValidAddress = row[10] == ''

                correctAddress = row[10]

                addressCorrectedAt = ClockTime("08:00 AM" if isValidAddress else row[11])

                deliveredWith = {int(item) for item in row[12].split(';') if item.isdigit()}

                # Create a Package object using the extracted data
                package = Package(id, addressId, address, city, state, zip_code, deadline, weight, truckId, arrivedAt, isValidAddress, correctAddress, addressCorrectedAt, deliveredWith)
                packages.append(package)
    return packages

