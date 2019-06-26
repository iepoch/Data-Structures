class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # first to pop anything off the heap. Swap the Max value to end of heap
        # delete this value and save it - return it as a max value
        # then bubble down the value at index 0 to it's proper position
        removed = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(0)
        return removed

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # check if the index is greater than zero
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent  # updating the new index
            else:
                break

        # grab the parent index
        # check if current value is greater than or less than parent value

    def _sift_down(self, index):
        left = index * 2
        right = index * 2 + 1

        largest = index
        if index == 0:
            return None
        if self.get_max > left and self.storage[largest] < self.storage[left]:
            largest = left
        if self.get_max > right and self.storage[largest] < self.storage[right]:
            largest = right
        if largest != index:
            self.storage[index], self.storage[largest] = self.storage[largest], self.storage[index]
            self._sift_down(largest)
