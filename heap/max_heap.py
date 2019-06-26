class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        # first to pop anything off the heap. Swap the Max value to end of heap
        # delete this value and save it - return it as a max value
        # then bubble down the value at index 0 to it's proper position\
        if self.storage is None:
            return None
        removed = self.storage[0]
        print(removed)
        self.storage[0] = self.storage[self.get_size()- 1]
        print(self.storage[0])
        self.storage.pop()
        print(self.storage)
        self._sift_down(0)
        # print(self._sift_down)
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
       while index * 2 + 1 <= self.get_size() - 1:
            largest = self._max_child(index)
            if self.storage[index] < self.storage[largest]:
                self.storage[index], self.storage[largest] = self.storage[largest], self.storage[index]
            index = largest
    #added function _max_child  to get the maxium size of the child and maintain the order of the heap
    def _max_child(self, index):
        right = index * 2 + 2 
        left = index * 2 + 1
        if right > self.get_size() - 1:
            return left
        else:
            return left if self.storage[left] > self.storage[right] else right
