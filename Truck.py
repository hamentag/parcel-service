
class Truck:
    TRUCK_MAX_CAPACITY = 16
    def __init__(self, id, maxCapacity = TRUCK_MAX_CAPACITY):
        self.id = id
        self.maxCapacity = maxCapacity
        self.packages = []

    def isNotFull(self):
        return len(self.packages) < self.maxCapacity
        
    def isNotFullAfterAdding(self, additionalPackages):
        return (len(self.packages) + additionalPackages) <= self.maxCapacity
    
    def __repr__(self):
        packages_repr = ', '.join([repr(package) for package in self.packages])
        return f"Truck(id={self.id}, maxCapacity={self.maxCapacity}, packages=[{packages_repr}])"
