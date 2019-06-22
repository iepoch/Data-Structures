"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None): 
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        if self.head == None:
            return None
        else:
            old_head = self.head
            self.head.delete()
            self.head = old_head.prev
        return old_head.value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        if self.head == None and self.tail == None:
            return None
        else:
            value= self.tail
            self.tail.delete()
            return self.tail.value
    def move_to_front(self, node):
        value = node.value
        node.delete()
        self.add_to_head(value)
            # pass

    def move_to_end(self, node):
        value = node.value
        node.delete()
        self.add_to_tail(value)


    def delete(self, node):
           return node.delete()
            
    def get_max(self):

            cur_max = self.head.value
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
                if cur_node.value > cur_max:
                    cur_max = cur_node.value
                #if we find a node > cur_max update cur_max 
            
            return cur_max
        # pass
