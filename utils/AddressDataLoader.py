import csv
from Address import Address
from data.Constants import ADDRESS_FILE_PATH

# Read package data from CSV file and return a list of Address objects.
def read_address_csv_file():
    addresses = []
    with open(ADDRESS_FILE_PATH, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        # Skip the first line (header)
        # next(csv_reader)

        for row in csv_reader:
            if row:  # Skip empty rows
                id = int(row[0])
                place = row[1]
                address = row[2]
                city = row[3]
                state = row[4]
                zip = row[5]                  

                address = Address(id, place, address, city, state, zip)
                addresses.append(address)
    return addresses

# Insert addresses into the hash table
def load_addresses_data(address_hash_table):
    for address in read_address_csv_file():
        address_hash_table.insert(address.id, address)


