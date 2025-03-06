
# Partition function for QuickSort
def sort(list, start_index, end_index, get_value):
    def partition(list, start_index, end_index):
        midpoint = start_index + (end_index - start_index) // 2
        pivot = get_value(list[midpoint])                # Get value of the sorting criterion

        low = start_index
        high = end_index
        done = False
        
        while not done:
            while get_value(list[low]) < pivot:
                low = low + 1

            while pivot < get_value(list[high]):
                high = high - 1

            if low >= high:
                done = True
            else:
                # Swap
                list[low], list[high] = list[high], list[low]
                low = low + 1
                high = high - 1

        return high

    # Quicksort function to sort distances
    def quicksort(list, start_index, end_index):
        if end_index <= start_index:
            return

        # Partition the list of distances
        high = partition(list, start_index, end_index)

        # Recursively sort the left segment
        quicksort(list, start_index, high)

        # Recursively sort the right segment
        quicksort(list, high + 1, end_index)

    quicksort(list, start_index, end_index)

