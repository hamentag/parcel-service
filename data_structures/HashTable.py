#########################################################
# Repository: https://github.com/hamentag/parcel-service

#########################################################
# Citation: 
# (Lysecky & Vahid, 2022, ch. 4, paras. 4.10 & 4.10)
# (Lysecky & Vahid, 2022, ch. 6, para. 6.7)

#########################################################
## For Time and Space Complexity:
# n: The number of elements.

#########################################################
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize the table

    # Hash function to calculate the index for a given key.
    # Time Complexity: O(1), Space Complexity: O(1)
    def _hash(self, key):
        return key % self.size
    
    # Insert an element into the hash table
    # Time Complexity: O(1). Space Complexity: O(1).   
    def insert(self, newElementId, newElement):
        index = self._hash(newElementId)    # Compute the index based on the element ID
        found = False
        for el in self.table[index]:    # Traverse the bucket to check if element with the same ID exists
            if el.id == newElementId:
                el = newElement       # Update the existing element if found
                found = True
                break
        if not found:
            self.table[index].append(newElement)  

    
    # Delete an element from the hash table by element ID
    # Time Complexity: O(1). Space Complexity: O(1). 
    def delete(self, elementId):
        index = self._hash(elementId)
        for i, el in enumerate(self.table[index]):
            if el.id == elementId:
                del self.table[index][i]
                return True
        print(f"Element with ID {elementId} not found.")
        return False


    # Lookup an element in the hash table by element ID
    # Time Complexity: O(1). Space Complexity: O(1).  
    def lookup(self, elementId):
        index = self._hash(elementId)
        for el in self.table[index]:
            if el.id == elementId:
                return el
        print(f"Element with ID {elementId} not found.")
        return None  # if not found
    
    # Return a list of all elements IDs in the hash table
    # Time Complexity: O(n). Space Complexity: O(n).
    def get_all_element_ids(self):
        elementIds = []
        for entry in self.table:      # Traverse each bucket
            for el in entry:            # Traverse each element in the bucket
                elementIds.append(el.id)
        return elementIds
    
    # Display the hash table
    # Time Complexity: O(n). Space Complexity: O(1).
    def display(self):
        for i, entry in enumerate(self.table):
            print(f"Entry {i}: {entry}")

