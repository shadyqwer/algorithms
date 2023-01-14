import math


class ListSorting:
    def __init__(self, unsorted):
        self.unsorted = unsorted

    # O(n^2), loop through elements and swap places if needed
    def bubble_sort(self, sorted_list=None, ascending=True):
        if sorted_list is None:
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
    def selection_sort(self, sorted_list=None, ascending=True):
        if sorted_list is None:
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
    def insertion_sort(self, sorted_list=None, ascending=True):
        if sorted_list is None:
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
    def heap_sort(self, unsorted=None, ascending=True):

        if unsorted is None:
            unsorted = self.unsorted.copy()

        def heapify(arr, size, inx, ascend):
            left = 2 * inx + 1
            right = 2 * inx + 2
            node = inx
            if ascend:
                if left < size and arr[inx] < arr[left]:
                    node = left
                if right < size and arr[node] < arr[right]:
                    node = right
                if node != inx:
                    arr[inx], arr[node] = arr[node], arr[inx]
                    heapify(arr, size, node, ascend)
            else:
                if left < size and arr[inx] > arr[left]:
                    node = left
                if right < size and arr[node] > arr[right]:
                    node = right
                if node != inx:
                    arr[inx], arr[node] = arr[node], arr[inx]
                    heapify(arr, size, node, ascend)

        def heap(arr, ascend):
            heap_size = len(arr)
            for i in range(heap_size // 2 - 1, -1, -1):
                heapify(arr, heap_size, i, ascend)

            for i in range(heap_size - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0, ascend)

            return arr

        return heap(unsorted, ascending)

    # O(N logN), worst case O(N^2), largely depends on pivot selection
    def quick_sort(self, unsorted=None, ascending=True):
        if unsorted is None:
            unsorted = self.unsorted.copy()
        if len(unsorted) <= 1:
            return unsorted

        def quick(arr, low, high, ascend):
            if low < high:
                pivot = partition(arr, low, high, ascend)
                quick(arr, low, pivot - 1, ascend)
                quick(arr, pivot + 1, high, ascend)
            return arr

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
            arr[pivot_inx], arr[low] = arr[low], arr[pivot_inx]  # pivot is always placed at 0 index
            border = low  # set border to pivot

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

        return quick(unsorted, 0, len(self.unsorted) - 1, ascending)

    # O(N logN), recursive, divide and conquer
    def merge_sort(self, unsorted=None, ascending=True):
        if unsorted is None:
            unsorted = self.unsorted.copy()

        def merge(arr, ascend=ascending):
            sorted_list = []
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left = merge(arr[:mid], ascend)
            right = merge(arr[mid:], ascend)
            i = j = 0
            while i < len(left) and j < len(right):
                if ascend:
                    if left[i] < right[j]:
                        sorted_list.append(left[i])
                        i += 1
                    else:
                        sorted_list.append(right[j])
                        j += 1
                else:
                    if left[i] > right[j]:
                        sorted_list.append(left[i])
                        i += 1
                    else:
                        sorted_list.append(right[j])
                        j += 1
            sorted_list += left[i:]
            sorted_list += right[j:]
            return sorted_list

        return merge(unsorted)

    # O(N + k), where k is length of the longest number in list
    # worst O(N^2)
    # divide elements into buckets, sort using quick/insertion sort, put back together
    def bucket_sort(self, unsorted=None, ascending=True):
        if unsorted is None:
            unsorted = self.unsorted.copy()
        if len(unsorted) <= 1:
            return unsorted

        low, high = min(unsorted), max(unsorted)
        no_buckets = int(math.sqrt(high - low))
        range_buckets = (high - low) // no_buckets
        buckets = [[] for _ in range(no_buckets)]
        for num in unsorted:
            inx = (num - low) // range_buckets
            inx -= 1 if num == high else 0
            buckets[inx].append(num)
        unsorted = []  # empty unsorted element to put buckets into
        if ascending:
            for bucket in buckets:
                unsorted += self.quick_sort(bucket, ascending=ascending)
        else:
            for d in range(len(buckets) - 1, -1, -1):
                unsorted += self.quick_sort(buckets[d], ascending=ascending)
        return unsorted

    # O(N * k), k - length of the longest number in list
    # uses number of buckets equal to k
    def radix_sort(self, unsorted=None, ascending=True):
        if unsorted is None:
            unsorted = self.unsorted.copy()
        k = len(str(max(unsorted, default=0)))
        for digit in range(k):
            buckets = [[] for _ in range(10)]
            e = 10 ** digit
            for num in unsorted:
                buckets[num // e % 10].append(num)
            unsorted = []
            if ascending:
                for bucket in buckets:
                    unsorted += bucket
            else:
                for d in range(len(buckets) - 1, -1, -1):
                    unsorted += buckets[d]
        return unsorted

    # O(N + k), where k is range between lowest and highest element
    def counting_sort(self, unsorted=None, ascending=True):
        if unsorted is None:
            unsorted = self.unsorted.copy()
        # needed for negative numbers
        low = min(unsorted)
        high = max(unsorted)
        count = [[] for _ in range(low, high + 1)]
        result = []
        for item in unsorted:
            count[item - low].append(item)
        if ascending:
            for asc in count:
                result += asc
        else:
            for d in range(len(count) - 1, -1, -1):
                result += count[d]
        return result

    def __str__(self):
        s = 'Unsorted list: ' + ', '.join(map(str, self.unsorted))
        return s
