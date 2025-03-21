class Address:
    def __init__(self, id, place, address, city, state, zip):
        self.id = id
        self.place = place
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

        self.packages = set()
    
    def __repr__(self):
        packages_repr = ', '.join([repr(pck) for pck in self.packages])
        return f"Address(id={self.id}, place={self.place}, address={self.address}, city={self.city}, state={self.state}, zip={self.zip}, packages=[{packages_repr}])"
