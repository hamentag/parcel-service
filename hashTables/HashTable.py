
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize the table

    def _hash(self, key):
        return key % self.size
    
    
    # Insert an element into the hash table
    def insert(self, newElementId, newElement):
        index = self._hash(newElementId)
        found = False
        for el in self.table[index]:
            if el.id == newElementId:
                el = newElement           # update existing element
                found = True
                break
        if not found:
            self.table[index].append(newElement)  

    
    # Delete an element from the hash table by element ID
    def delete(self, elementId):
        index = self._hash(elementId)
        for i, el in enumerate(self.table[index]):
            if el.id == elementId:
                del self.table[index][i]
                return True
        print(f"Element with ID {elementId} not found.")
        return False


    # Lookup an element in the hash table by element ID
    def lookup(self, elementId):
        index = self._hash(elementId)
        for el in self.table[index]:
            if el.id == elementId:
                return el
        print(f"Element with ID {elementId} not found.")
        return None  # if not found
    
    # Return a list of all elements IDs in the hash table
    def getAllElementIds(self):
        elementIds = []
        for entry in self.table:
            for el in entry:
                elementIds.append(el.id)
        return elementIds
    
    # Display the hash table
    def display(self):
        for i, entry in enumerate(self.table):
            print(f"Entry {i}: {entry}")

