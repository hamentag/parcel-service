from TruckStatus import TruckStatus
from data.Constants import TRUCK_MAX_CAPACITY, TRUCK_SPEED
class Truck:
    def __init__(self, id, hub, maxCapacity = TRUCK_MAX_CAPACITY, speed = TRUCK_SPEED):
        self.id = id
        self.hub = hub
        self.maxCapacity = maxCapacity
        self.packages = set()
        self.mileage = 0.0
        self.speed = speed
        self.status = TruckStatus(self)

        self.hub.trucks.append(self)


    def isNotFull(self):
        return len(self.packages) < self.maxCapacity
    
    def isFull(self):
        return len(self.packages) >= self.maxCapacity
        
    def isNotFullAfterAdding(self, additionalPackages):
        return (len(self.packages) + additionalPackages) <= self.maxCapacity
    
    def is_overloaded_by_adding(self, additionalPackages):
        return (len(self.packages) + additionalPackages) > self.maxCapacity
    
    def add_packages(self, group):
        for pck in group:
            if self.isFull():
                return
            self.packages.append(pck)           # add_single_package
            # self.hub.packages.remove(pck)

    def add_single_package(self, package_id):
        if self.isFull():
            return
        self.packages.add(package_id)
        # self.hub.packages.remove(package_id)



    def __repr__(self):
        return f"Truck(id={self.id}, lenOfPck={len(self.packages)}, maxCapacity={self.maxCapacity}, mileage={self.mileage}, status={self.status}, packages={repr(self.packages)})"
