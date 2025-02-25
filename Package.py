from ClockTime import ClockTime
class Package:
    def __init__(self, id, addressId, address, deadline, weight, truckId, correctAddress, deliveredWith, status):
        self.id = id
        self.addressId = addressId
        self.address = address
    
        self.deadline = deadline
        self.weight = weight
        
        self.truckId = truckId

        self.correctAddress = correctAddress

        self.deliveredWith = deliveredWith

        self.status = status

    
    
    def __repr__(self):
        return f"Package(id={self.id}, addressId={self.addressId}, address={self.address}, " \
        f"deadline={self.deadline}, weight={self.weight}, truckId={self.truckId}, correctAddress={self.correctAddress}, " \
        f"deliveredWith={self.deliveredWith}, status={self.status})"
