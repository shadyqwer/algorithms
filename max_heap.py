class MaxHeap:
    def __init__(self, items):
        if items is None:
            items = []
        self.heap = [None]
        for i in items:
            self.heap.append(i)
            self.move_up(len(self.heap) - 1)

    def push(self, node):
        self.heap.append(node)
        self.move_up(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max_val = self.heap.pop()
            self.heapify(1)
        elif len(self.heap) == 2:
            max_val = self.heap.pop()
        else:
            max_val = False
        return max_val

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def move_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] >> self.heap[parent]:
            self.__swap(index, parent)
            self.move_up(parent)

    def heapify(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if left < len(self.heap) and self.heap[largest] < self.heap[left]:
            largest = left
        if right < len(self.heap) and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.heapify(largest)

    def __str__(self):
        return ', '.join(map(str, self.heap[1:]))