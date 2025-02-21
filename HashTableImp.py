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

    
    def display(self):
        """ Display the hash table """
        for i, entry in enumerate(self.table):
            print(f"Entry {i}: {entry}")