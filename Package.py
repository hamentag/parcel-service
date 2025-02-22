from ClockTime import ClockTime
class Package:
    def __init__(self, id, addressId, address, deadline, weight, truckId, arrivedAt, isValidAddress, correctAddress, addressCorrectedAt, deliveredWith):
        self.id = id
        self.addressId = addressId
        self.address = address
    
        self.deadline = deadline
        self.weight = weight
        
        self.truckId = truckId
        self.arrivedAt = arrivedAt

        self.outForDeliveryAt = None

        self.isValidAddress = isValidAddress
        self.correctAddress = correctAddress
        self.addressCorrectedAt = addressCorrectedAt

        self.deliveredWith = deliveredWith

        # self.status = "At the hub" if arrivedAt ==  "08:00 AM" else "Not Available"
        self.status = "At the hub"

    def isArrivedAt(self,thisTime):  # TODO: thisTime is object ClockTime or str? 
        #t = ClockTime(thisTime)
        if thisTime.isBefore(self.arrivedAt):
            return False
        return True
    def isValidAddressAt(self,thisTime):  # TODO: thisTime is object ClockTime or str? 
        if self.isValidAddress:
            return True
        #t = ClockTime(thisTime)
        if thisTime.isBefore(self.addressCorrectedAt):
            return False
        return True

    def isAvailableAt(self, thisTime):
        return self.isArrivedAt(thisTime) and self.isValidAddressAt(thisTime)
        
    
    def __repr__(self):
        return f"Package(id={self.id}, addressId={self.addressId}, address={self.address}, " \
        f"deadline={self.deadline}, weight={self.weight}, truckId={self.truckId}, arrivedAt={self.arrivedAt}, " \
        f"outForDeliveryAt={self.outForDeliveryAt}, isValidAddress={self.isValidAddress}, correctAddress={self.correctAddress}, " \
        f"addressCorrectedAt={self.addressCorrectedAt}, deliveredWith={self.deliveredWith}, status={self.status})"
