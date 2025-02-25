from utils.QuicksortFunction import quicksort

class DistanceHashTable:
    def __init__(self):
        self.data = {}

    def _normalize_key(self, x, y):
        return (min(x, y), max(x, y))

    def insert(self, addr1, addr2, distance):
        row, col = self._normalize_key(addr1, addr2)

        if row not in self.data:
            self.data[row] = {}     # create a new dictionary for the row

        self.data[row][col] = distance      # Insert the value

    def lookup(self, addr1, addr2):
        row, col = self._normalize_key(addr1, addr2)

        if row in self.data and col in self.data[row]:
            return self.data[row][col]
        else:
            return None  # combination doesn't exist

    def delete(self, addr1, addr2):
        row, col = self._normalize_key(addr1, addr2)

        # Check if the row and column exist in the dictionary
        if row in self.data and col in self.data[row]:
            del self.data[row][col]
            # If the row becomes empty after deletion, remove the row entirely
            if not self.data[row]:
                del self.data[row]
            return True
        else:
            return False 
    def display(self):
        if not self.data:
            print("The distance hash table is empty.")
            return
        
        for row, cols in self.data.items():
            for col, distance in cols.items():
                print(f"Distance between {row} and {col} is {distance}")

   
    ###############
    def get_all_distances(self, addr):
        distances = []
        for row, cols in self.data.items():
            for col, distance in cols.items():
                # If the address is part of the pair (either as row or column)
                if addr == row:
                    distances.append((col, distance))  # (other address, distance)
                elif addr == col:
                    distances.append((row, distance))  # (other address, distance)

        if distances:
            return distances
        else:
            return f"No distances found for address {addr}."
        

    ###########################
    def get_sorted_distances(self, addr, address_list):
        distances = []
        for other_addr in address_list:
            distance = self.lookup(addr, other_addr)
            # if distance is None:
            #     distances.append(f"No distance found for {addr} and {other_addr}")
            # else:
            #     distances.append(distance)
            if distance is not None:
                distances.append((other_addr, distance))
                
        quicksort(distances, 0, len(distances) - 1)

        return distances
    
    ######################################
    

