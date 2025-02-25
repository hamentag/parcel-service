import csv
from Package import Package
from ClockTime import ClockTime
from Status import Status

# Read package data from CSV file and return a list of Package objects.
def readPackagesData(file_path):
    packages = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Skip empty rows
                id = int(row[0])                
                addressId = row[1]
                address = row[2]
                

                # EOD = 11:59 PM
                deadline = ClockTime("11:59 PM" if row[3] == "EOD" else row[3])

                weight = row[4]
                
                truckId = int(row[5]) if  row[5] != '' else -1   # truckId = 0, 1, or 2

                arrivedAt = ClockTime("08:00 AM" if row[6] == '' else row[6])


                isValidAddress = row[7] == ''

                correctAddress = row[7]

                addressCorrectedAt = ClockTime("08:00 AM" if isValidAddress else row[8])

                deliveredWith = {int(item) for item in row[9].split(';') if item.isdigit()}

                status = Status(deadline, arrivedAt, isValidAddress, addressCorrectedAt)

                # Create a Package object using the extracted data
                package = Package(id, addressId, address, deadline, weight, truckId, correctAddress, deliveredWith, status)
                packages.append(package)
    return packages

