
# class Quicksorter:
#     def __init__(self, packageHashTable):
#         self.packageHashTable = packageHashTable
            
#     def get_deadline(self, package_id):
#         package = self.packageHashTable.lookup(package_id)
#         if package is not None:
#             return package.deadline
#     # Partition function for QuickSort
#     def partition(self, pcks, start_index, end_index):
#         midpoint = start_index + (end_index - start_index) // 2
#         pivot = self.get_deadline(pcks[midpoint])

#         low = start_index
#         high = end_index
#         done = False
        
#         while not done:
#             while self.get_deadline(pcks[low]).is_before(pivot):     # while pcks[low][1] < pivot:   
#                 low = low + 1

#             while pivot.is_before(self.get_deadline(pcks[high])):                    # while pivot < pcks[high][1]:
#                 high = high - 1

#             if low >= high:
#                 done = True
#             else:
#                 # Swap
#                 pcks[low], pcks[high] = pcks[high], pcks[low]
#                 # temp = numbers[low]
#                 # numbers[low] = numbers[high]
#                 # numbers[high] = temp
#                 low = low + 1
#                 high = high - 1

#         return high

#     # Quicksort function to sort distances
#     def quicksort(self, pcks, start_index, end_index):
#         if end_index <= start_index:
#             return

#         # Partition the list of distances
#         high = self.partition(pcks, start_index, end_index)

#         # Recursively sort the left segment
#         self.quicksort(pcks, start_index, high)

#         # Recursively sort the right segment
#         self.quicksort(pcks, high + 1, end_index)



# Partition function for QuickSort
def sort(pcks, start_index, end_index, get_deadline):
    def partition(pcks, start_index, end_index):
        midpoint = start_index + (end_index - start_index) // 2
        pivot = get_deadline(pcks[midpoint])

        low = start_index
        high = end_index
        done = False
        
        while not done:
            while get_deadline(pcks[low]).is_before(pivot):     # while pcks[low][1] < pivot:   
                low = low + 1

            while pivot.is_before(get_deadline(pcks[high])):                    # while pivot < pcks[high][1]:
                high = high - 1

            if low >= high:
                done = True
            else:
                # Swap
                pcks[low], pcks[high] = pcks[high], pcks[low]
                # temp = numbers[low]
                # numbers[low] = numbers[high]
                # numbers[high] = temp
                low = low + 1
                high = high - 1

        return high

    # Quicksort function to sort distances
    def quicksort(pcks, start_index, end_index):
        if end_index <= start_index:
            return

        # Partition the list of distances
        high = partition(pcks, start_index, end_index)

        # Recursively sort the left segment
        quicksort(pcks, start_index, high)

        # Recursively sort the right segment
        quicksort(pcks, high + 1, end_index)

    quicksort(pcks, start_index, end_index)

