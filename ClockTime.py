import time

class ClockTime:
    def __init__(self, time_str):
        self.format_string = "%I:%M %p"
        self.time_str = time_str
        self.value = time.strptime(time_str, self.format_string)
    
    # Display clock time object
    def __repr__(self):
        return f"ClockTime({self.time_str})"
    

    # Returns the time as a string in 'HH:MM AM/PM' format.
    def get_time_str(self):
        return time.strftime("%I:%M %p", self.value)
    
    
    # Compares the current time object with another ClockTime object
    def isBefore(self, other):
        # Convert both times to minutes from the start of the day (00:00)
        current_time_minutes = self.value.tm_hour * 60 + self.value.tm_min
        other_time_minutes = other.value.tm_hour * 60 + other.value.tm_min
        
        return current_time_minutes <= other_time_minutes
    def is_before(self, other):
        # Convert both times to minutes from the start of the day (00:00)
        current_time_minutes = self.value.tm_hour * 60 + self.value.tm_min
        other_time_minutes = other.value.tm_hour * 60 + other.value.tm_min
        
        return current_time_minutes < other_time_minutes            ######## <<<<<<<<<<<<
    
    # Compares the current time object with a time string in 'HH:MM AM/PM' format
    def isBeforeWithStr(self, time_str):
        # Parse the string time to a struct_time
        other_time = time.strptime(time_str, self.format_string)
        
        # Convert both times to minutes from the start of the day (00:00)
        current_time_minutes = self.value.tm_hour * 60 + self.value.tm_min
        other_time_minutes = other_time.tm_hour * 60 + other_time.tm_min
        
        return current_time_minutes < other_time_minutes
    
    
    
    # Calculate the arrival time based on distance and speed using the object's time
    def get_arrival_time(self, time_to_travel_minutes):
        # Get current hour and minute from the current ClockTime object (self)
        current_hour = self.value.tm_hour
        current_minute = self.value.tm_min
        
        # Add travel time to current time (in minutes)
        total_minutes = (current_hour * 60 + current_minute) + time_to_travel_minutes
        
        # Calculate the new hour and minute
        arrival_hour = (total_minutes // 60) % 24  # Hour within a 24-hour period
        arrival_minute = total_minutes % 60
        
        # Convert back to 12-hour format for AM/PM
        if arrival_hour >= 12:
            period = "PM"
            if arrival_hour > 12:
                arrival_hour -= 12
        else:
            period = "AM"
            if arrival_hour == 0:
                arrival_hour = 12
        
        # Format the time as a string for the new ClockTime object
        # arrival_time_str = f"{arrival_hour:02}:{arrival_minute:02} {period}"
        arrival_time_str = f"{int(arrival_hour):02}:{int(arrival_minute):02} {period}"
        
        # Return the arrival time as a new ClockTime object
        return ClockTime(arrival_time_str)
        # return arrival_time_str
        
