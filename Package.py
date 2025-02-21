class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, truckId, availableAt, isValidAddress, correctAddress, addressCorrectedAt, deliveredWith):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        
        self.truckId = truckId
        self.availableAt = availableAt

        self.isValidAddress = isValidAddress
        self.correctAddress = correctAddress
        self.addressCorrectAt = addressCorrectedAt

        self.deliveredWith = deliveredWith

        self.status = "At the hub" if availableAt ==  "08:00 AM" else "Not Available"
    
    def __repr__(self):
        return f"Package(id={self.id}, address={self.address}, city={self.city}, state={self.state}, zip={self.zip}, " \
        f"deadline={self.deadline}, weight={self.weight}, truckId={self.truckId}, availableAt={self.availableAt}, " \
        f"isValidAddress={self.isValidAddress}, correctAddress={self.correctAddress}, " \
        f"addressCorrectedAt={self.addressCorrectAt}, deliveredWith={self.deliveredWith}, status={self.status})"
