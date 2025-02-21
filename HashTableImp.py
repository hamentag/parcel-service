from Package import Package

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize the table

    def _hash(self, key):
        return key % self.size      

    def insert(self, packageId, package):
        index = self._hash(packageId)

        found = False
        for p in self.table[index]:
            if p.id == packageId: 
                p = package
                found = True
                break
        if not found:
            self.table[index].append(package)  
        print(f"Inserted package with ID {packageId} into index {index}")

    def delete(self, packageId, package):
        index = self._hash(packageId)
        for i, p in enumerate(self.table[index]):
            if p.id == packageId:
                del self.table[index][i]
                print(f"Deleted package with ID {packageId} from index {index}")
                return True
        print(f"Package with ID {packageId} not found.")
        return False

    def lookup(self, packageId):
        index = self._hash(packageId)
        for p in self.table[index]:
            if p.id == packageId:
                print(f"Found package with ID {packageId} at index {index}")
                return p 
        print(f"Package with ID {packageId} not found.")
        return None  # not found
    
    def get_all_package_ids(self):
        """ Return a list of all package IDs in the hash table """
        package_ids = []
        for entry in self.table:
            for p in entry:
                package_ids.append(p.id)
        return package_ids

    def display(self):
        """ Display the hash table """
        for i, entry in enumerate(self.table):
            print(f"Entry {i}: {entry}")

