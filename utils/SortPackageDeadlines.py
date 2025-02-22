# SortPackageDeadlines.py

# Function to convert a time string from hh:mm AM/PM format to 24-hour hh:mm format
def to_24hr_format(time_str):
    time_part, period = time_str.split()
    hour, minute = map(int, time_part.split(':'))
    
    if period == "AM":
        if hour == 12:
            hour = 0  # Midnight case (12:xx AM becomes 00:xx)
    else:  # PM
        if hour != 12:
            hour += 12  # PM times (except 12 PM) should be converted to 24-hour format
    
    return f"{hour:02}:{minute:02}"

# Function to extract the "digit" (index) from a time string based on a given position
def get_time_digit(deadline_str, position):
    if deadline_str == "EOD":
        deadline_str = "11:59 PM"
    
    deadline_str_24hr = to_24hr_format(deadline_str)
    hour, minute = map(int, deadline_str_24hr.split(':'))
    
    if position == 0:
        return minute % 10
    elif position == 1:
        return (minute // 10) % 10
    elif position == 2:
        return hour % 10
    elif position == 3:
        return (hour // 10) % 10

# Function to sort the packages based on deadline
def sort_package_deadlines(packages):
    max_digits = 4
    
    for digit_index in range(max_digits):
        buckets = [[] for _ in range(10)]
        
        for package in packages:
            digit = get_time_digit(package.deadline, digit_index)
            buckets[digit].append(package)
        
        packages.clear()
        for bucket in buckets:
            packages.extend(bucket)
