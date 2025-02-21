import csv
from Package import Package
from ClockTime import ClockTime


def read_packages_from_csv(file_path):
    packages = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  
                id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zip_code = row[4]

             
                deadline = ClockTime("11:59 PM" if row[5] == "EOD" else row[5])

                weight = row[6]
                
                truckId = int(row[7]) if  row[7] != '' else -1 

                availableAt = ClockTime("08:00 AM" if row[8] == '' else row[8])

                isValidAddress = row[9] == ''

                correctAddress = row[9]

                addressCorrectedAt = ClockTime("08:00 AM" if isValidAddress else row[10])

                deliveredWith = {int(item) for item in row[11].split(';') if item.isdigit()}

               
                package = Package(id, address, city, state, zip_code, deadline, weight, truckId, availableAt, isValidAddress, correctAddress, addressCorrectedAt, deliveredWith)
                packages.append(package)
    return packages