class Address:
    def __init__(self, id, place, address, city, state, zip):
        self.id = id
        self.place = place
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
    
    def __repr__(self):
        return f"Address(id={self.id}, place={self.place}, address={self.address}, city={self.city}, state={self.state}, zip={self.zip})"
