class Hub:
    _id_counter = 1
    def __init__(self, id=None):
        if id is None:
            self.id = Hub._id_counter
            Hub._id_counter += 1
        else:
            self.id = id

        self.trucks = []
        self.packages = []
        
    
    def __repr__(self):
        trucks_repr = ', '.join([repr(truck) for truck in self.trucks])
        packages_repr = ', '.join([repr(package) for package in self.packages])
        return f"Hub(id={self.id}, trucks=[{trucks_repr}], packages=[{packages_repr}])"
