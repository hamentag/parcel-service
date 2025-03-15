import csv

def normalize_key(x, y):
    return (max(x, y), min(x, y))

def read_distance(addr1, addr2):
    key = normalize_key(addr1, addr2)
    
    with open('data/Distance_File.csv', mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        for row_index, row in enumerate(csv_reader):
            if row_index == key[0]:
                return float(row[key[1]])
    
    # If the key is not found
    return None
