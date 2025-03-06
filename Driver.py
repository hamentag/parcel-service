
class Driver:
    def __init__(self, id, hub):
        self.id = id
        self.hub = hub
        self.truck_assignments = []
    def allocate(self, truck, time):
        self.truck_assignments.append((truck.id, time.get_time_str()))  #

    def __repr__(self):
        truck_assignments_repr = ', '.join([repr(assignment) for assignment in self.truck_assignments])
        return f"Driver(id={self.id}, hub={self.hub.name}, truck_assignments=[{truck_assignments_repr}])"
