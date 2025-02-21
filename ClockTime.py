import time

class ClockTime:
    def __init__(self, time_str):
        self.format_string = "%I:%M %p"
        self.time_str = time_str
        self.value = time.strptime(time_str, self.format_string)
    
   
    def __repr__(self):
        return f"ClockTime({self.time_str})"
    
