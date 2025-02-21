class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, truckId, status="At the hub"):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        
        self.truckId = truckId

    
    def __repr__(self):
        return f"Package(id={self.id}, address={self.address}, city={self.city}, state={self.state}, zip={self.zip}, " \
        f"deadline={self.deadline}, weight={self.weight}, truckId={self.truckId}, status={self.status})"
