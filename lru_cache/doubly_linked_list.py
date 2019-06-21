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
      # create a  'ListNode' w/value
      # node.next -> insert new value
      # self.head.prev -> Update the Previous Node first
      # self.head   -> set the value with new node value
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        if self.head == None:
            return None
        node = self.head
        self.head.delete()
        self.head = node.next
        return node.value

    def add_to_tail(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove_from_tail(self):
        if self.tail == None:
            node_tail = self.tail
            node_tail.delete()
            self.tail = node_tail.prev
            return node_tail.value

    def move_to_front(self, node):
            # remove 'node' ... ListNode delete () But need to save value 1st
        value = node.value  # set value to 2
        node.delete()
        self.add_to_head(value)
        # add 'node' to head ... addtohead()

    def move_to_end(self, node):
            # remove 'node' ... ListNode delete () But need to save value 1st
        value = node.value  # set value to 2
        node.delete()

        self.add_to_tail(value)

    def delete(self, node):
        node.delete()

    def get_max(self):
        if self.head == None:
            return None
        else:
            curr_max = self.head.value
            cur_node = self.head
            # loop through nodes until reach tail
            while cur_node.next:
                cur_node = cur_node.next
                # if we find a node > cur_max, update cur_max
                if cur_node.value > curr_max:
                    curr_max = cur_node.value

            return curr_max
