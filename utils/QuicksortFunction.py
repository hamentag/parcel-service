
# Partition function for QuickSort
def partition(distances, start_index, end_index):
    midpoint = start_index + (end_index - start_index) // 2
    pivot = distances[midpoint][1]

    low = start_index
    high = end_index
    done = False
    
    while not done:
        while distances[low][1] < pivot:
            low = low + 1

        while pivot < distances[high][1]:
            high = high - 1

        if low >= high:
            done = True
        else:
            # Swap distances
            distances[low], distances[high] = distances[high], distances[low]
            # temp = numbers[low]
            # numbers[low] = numbers[high]
            # numbers[high] = temp
            low = low + 1
            high = high - 1

    return high

# Quicksort function to sort distances
def quicksort(distances, start_index, end_index):
    if end_index <= start_index:
        return

    # Partition the list of distances
    high = partition(distances, start_index, end_index)

    # Recursively sort the left segment
    quicksort(distances, start_index, high)

    # Recursively sort the right segment
    quicksort(distances, high + 1, end_index)

