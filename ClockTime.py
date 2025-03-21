import time
from data.Constants import START_SHIFT
class ClockTime:
    format_string = "%I:%M %p"
    def __init__(self, time_str = START_SHIFT):
        self.time_str = time_str
        self.value = time.strptime(time_str, ClockTime.format_string)
    
    # Display clock time object
    def __repr__(self):
        return f"ClockTime({self.time_str})"


    # Returns the time as a string in 'HH:MM AM/PM' format.
    def get_time_str(self):
        return time.strftime("%I:%M %p", self.value)

    #
    def set_time_to_min_of(self, loading_sequences):
        if len(loading_sequences) == 0:
            return

        min_time = time.strptime(loading_sequences[0], ClockTime.format_string)
        min_index = 0
        
        for index, seq in enumerate(loading_sequences):
            seq_time = time.strptime(seq, ClockTime.format_string)
            if seq_time < min_time:
                min_time = seq_time
                min_index = index
        
        # Set the ClockTime object to the minimum time found
        self.time_str = time.strftime(ClockTime.format_string, min_time)
        self.value = min_time

        # Remove the minimum time from the list
        loading_sequences.pop(min_index)
    

    # Static method to calculate hours between two times in 'HH:MM AM/PM' format
    @staticmethod
    def hours_between(time1, time2):
        # Use value if time1 is a ClockTime object
        if isinstance(time1, ClockTime):
            time1 = time1.value
        else:
            time1 = time.strptime(time1, ClockTime.format_string)  # Parse string into struct_time

        if isinstance(time2, ClockTime):
            time2 = time2.value
        else:
            time2 = time.strptime(time2, ClockTime.format_string)  # Parse string into struct_time
        
    
        # Convert times to hours
        time1_hrs = time1.tm_hour + time1.tm_min / 60.0
        time2_hrs = time2.tm_hour + time2.tm_min / 60.0
        
        # Return the absolute difference in hours
        return abs(time1_hrs - time2_hrs)
    
    @staticmethod
    def calculate_distance(time1, time2, speed_mph):
        # Calculate the time difference in hours
        time_diff_hours = ClockTime.hours_between(time1, time2)
        
        # Calculate the distance (Distance = Speed * Time)
        distance = speed_mph * time_diff_hours
        return distance


    # Compares the current time object with another ClockTime object or time string in 'HH:MM AM/PM' format
    def __lt__(self, target_time):
        if isinstance(target_time, str):
            target_time = ClockTime(target_time)
        
        current_time_minutes = self.value.tm_hour * 60 + self.value.tm_min
        other_time_minutes = target_time.value.tm_hour * 60 + target_time.value.tm_min
        
        return current_time_minutes < other_time_minutes
    
    def __gt__(self, target_time):
        if isinstance(target_time, str):
            target_time = ClockTime(target_time)
        
        current_time_minutes = self.value.tm_hour * 60 + self.value.tm_min
        other_time_minutes = target_time.value.tm_hour * 60 + target_time.value.tm_min
        
        return current_time_minutes > other_time_minutes
    
    def __le__(self, target_time):
        if isinstance(target_time, str):
            target_time = ClockTime(target_time)
        
        current_time_minutes = self.value.tm_hour * 60 + self.value.tm_min
        other_time_minutes = target_time.value.tm_hour * 60 + target_time.value.tm_min
        
        return current_time_minutes <= other_time_minutes
    def __ge__(self, target_time):
        if isinstance(target_time, str):
            target_time = ClockTime(target_time)
        
        current_time_minutes = self.value.tm_hour * 60 + self.value.tm_min
        other_time_minutes = target_time.value.tm_hour * 60 + target_time.value.tm_min
        
        return current_time_minutes >= other_time_minutes
    
    def __eq__(self, target_time):
        if isinstance(target_time, str):
            target_time = ClockTime(target_time)
    
        current_time_minutes = self.value.tm_hour * 60 + self.value.tm_min
        other_time_minutes = target_time.value.tm_hour * 60 + target_time.value.tm_min
        
        return current_time_minutes == other_time_minutes

    # Add travel time to current time (in minutes)
    def add_travel_time(self, time_to_travel_minutes):
        # Get current hour and minute from the current ClockTime object (self)
        current_hour = self.value.tm_hour
        current_minute = self.value.tm_min
        
        #Calculate total minutes
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
        arrival_time_str = f"{int(arrival_hour):02}:{int(arrival_minute):02} {period}"

        self.time_str = arrival_time_str
        self.value = time.strptime(arrival_time_str, ClockTime.format_string)
        
        return self
