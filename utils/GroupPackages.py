# GroupPackages.py

# Function to group packages by the same deadline without using defaultdict
def group_packages_by_deadline(packages):
    grouped = {}  # Regular dictionary
    
    for package in packages:
        # If the deadline already exists in the dictionary, append to the list
        if package.deadline in grouped:
            grouped[package.deadline].append(package)
        else:
            # Otherwise, create a new list for that deadline
            grouped[package.deadline] = [package]
    
    # Convert the dictionary values into a list of lists
    return list(grouped.values())
