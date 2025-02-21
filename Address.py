class Address:
    def __init__(self, id, place, address, city, state, zip):
        self.id = id
        self.place = place
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

        self.packages = []    
    
    def __repr__(self):
        packages_repr = ', '.join([repr(package) for package in self.packages])
        return f"Address(id={self.id}, place={self.place}, address={self.address}, packages=[{packages_repr}])"

