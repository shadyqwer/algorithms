class ListSorting:
    def __init__(self, unsorted):
        self.unsorted = unsorted

    # O(n^2), loop through elements and swap places if needed
    def bubble_sort(self, ascending=True):
        sorted_list = self.unsorted.copy()
        if ascending:
            for i in range(len(sorted_list) - 1):
                for j in range(len(sorted_list) - 1 - i):
                    if sorted_list[j] > sorted_list[j + 1]:
                        sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        else:
            for i in range(len(sorted_list) - 1):
                for j in range(len(sorted_list) - 1 - i):
                    if sorted_list[j] < sorted_list[j + 1]:
                        sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        return sorted_list

    # O(n^2), find min/max item and place it at lowest unsorted index
    def selection_sort(self, ascending=True):
        sorted_list = self.unsorted.copy()
        if ascending:
            for i in range(0, len(sorted_list) - 1):
                inx = i
                for j in range(i + 1, len(sorted_list)):
                    if sorted_list[j] < sorted_list[inx]:
                        inx = j
                if inx != i:
                    sorted_list[i], sorted_list[inx] = sorted_list[inx], sorted_list[i]
        else:
            for i in range(0, len(sorted_list) - 1):
                inx = i
                for j in range(i + 1, len(sorted_list)):
                    if sorted_list[j] > sorted_list[inx]:
                        inx = j
                if inx != i:
                    sorted_list[i], sorted_list[inx] = sorted_list[inx], sorted_list[i]
        return sorted_list

    # O(n^2), compares each element and shifts until find right place
    def insertion_sort(self, ascending=True):
        sorted_list = self.unsorted.copy()
        if ascending:
            for i in range(1, len(sorted_list)):
                current = sorted_list[i]
                j = i - 1
                while j >= 0 and current < sorted_list[j]:
                    sorted_list[j + 1] = sorted_list[j]
                    j -= 1
                sorted_list[j + 1] = current
        else:
            for i in range(1, len(sorted_list)):
                current = sorted_list[i]
                j = i - 1
                while j >= 0 and current > sorted_list[j]:
                    sorted_list[j + 1] = sorted_list[j]
                    j -= 1
                sorted_list[j + 1] = current
        return sorted_list

    # O(N logN)
    def heap_sort(self, ascending=True):
        unsorted = self.unsorted

        def heapify(arr, size, inx, ascend):
            left = 2 * inx
            right = 2 * inx + 1

            node = inx
            if ascend:
                if left < size and arr[inx] > arr[left]:
                    node = left
                if right < size and arr[node] > arr[right]:
                    node = right
                if node != inx:
                    arr[inx], arr[node] = arr[node], arr[inx]
                    heapify(arr, size, node, ascend)
            else:
                if left < size and arr[inx] < arr[left]:
                    node = left
                if right < size and arr[node] < arr[right]:
                    node = right
                if node != inx:
                    arr[inx], arr[node] = arr[node], arr[inx]
                    heapify(arr, size, node, ascend)

        def heap(arr, ascend):
            arr = [None] + arr  # make things more clear
            heap_size = len(arr)
            for i in range(heap_size // 2, 0, -1):
                heapify(arr, heap_size, i, ascend)
            return arr[1:]
        return heap(unsorted, ascending)

    # O(N logN), worst case O(N^2), largely depends on pivot selection
    def quick_sort(self, ascending=True):
        def quick(unsorted, low, high, ascend):
            if low < high:
                pivot = partition(unsorted, low, high, ascend)
                quick(unsorted, low, pivot - 1, ascend)
                quick(unsorted, pivot + 1, high, ascend)
            return unsorted

        # get pivot, chose median between low, high and middle element of array
        def get_pivot(arr, low, high):
            mid = (low + high) // 2
            pivot = high
            if arr[low] < arr[mid]:
                pivot = mid
            elif arr[low] < arr[high]:
                pivot = low
            return pivot

        # move smaller/bigger elements left or right from pivot depends on order
        def partition(arr, low, high, ascend):
            pivot_inx = get_pivot(arr, low, high)
            pivot_val = arr[pivot_inx]
            arr[pivot_inx], arr[low] = arr[low], arr[pivot_inx] # pivot is always placed at 0 index
            border = low # set border to pivot

            for i in range(low, high + 1):
                if ascend:
                    # found smaller element, increase border index and place element there
                    # bigger ones will stay from right side of border
                    if arr[i] < pivot_val:
                        border += 1
                        arr[i], arr[border] = arr[border], arr[i]
                else:
                    # found bigger element, increase border index and place element there
                    # smaller ones will stay from right side of border
                    if arr[i] > pivot_val:
                        border += 1
                        arr[i], arr[border] = arr[border], arr[i]
            # replace border with pivot so it comes in middle
            arr[low], arr[border] = arr[border], arr[low]
            return border
        return quick(self.unsorted, 0, len(self.unsorted) - 1, ascending)

    # O(N logN), recursive, divide and conquer
    def merge_sort(self, ascending=True):

        def merge(unsorted, ascend=ascending):
            sorted_list = []
            if len(unsorted) == 1:
                return unsorted
            mid = len(unsorted) // 2
            left = merge(unsorted[:mid], ascend)
            right = merge(unsorted[mid:], ascend)
            l = r = 0
            while l < len(left) and r < len(right):
                if ascend:
                    if left[l] < right[r]:
                        sorted_list.append(left[l])
                        l += 1
                    else:
                        sorted_list.append(right[r])
                        r += 1
                else:
                    if left[l] > right[r]:
                        sorted_list.append(left[l])
                        l += 1
                    else:
                        sorted_list.append(right[r])
                        r += 1
            sorted_list += left[l:]
            sorted_list += right[r:]
            return sorted_list
        return merge(self.unsorted)

    def radix_sort(self):
        ...

    def __str__(self):
        s = 'Unsorted list: ' + ', '.join(map(str, self.unsorted))
        return s
