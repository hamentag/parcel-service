import csv

# Read distance data from CSV file and insert distances in the hash table.
def load_distance_data(file_path, distance_hash_table):
        
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        # Skip the first line (header)
        # next(csv_reader)

        for addr1, row in enumerate(csv_reader):
            if row:  # Skip empty rows
                for addr2, col in enumerate(row):
                    if col == '':
                        break
                    distance = float(col)
                    distance_hash_table.insert(addr1, addr2, distance)
