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
        
        return current_time_minutes < other_time_minutes
    
    # Compares the current time object with a time string in 'HH:MM AM/PM' format
    def isBeforeWithStr(self, time_str):
        # Parse the string time to a struct_time
        other_time = time.strptime(time_str, self.format_string)
        
        # Convert both times to minutes from the start of the day (00:00)
        current_time_minutes = self.value.tm_hour * 60 + self.value.tm_min
        other_time_minutes = other_time.tm_hour * 60 + other_time.tm_min
        
        return current_time_minutes < other_time_minutes
        
