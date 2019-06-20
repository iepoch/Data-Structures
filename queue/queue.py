from node import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_head(item)
        self.size += 1
        # return self.size

    def dequeue(self):
        item = self.storage.remove_from_head()
        self.size -= 1 if self.size > 0 else 0
        return item

    def len(self):
        return self.size
