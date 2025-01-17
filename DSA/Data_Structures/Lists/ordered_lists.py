class Node:
    """A node of a linked list"""
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)
    

class OrderedList:
    def __init__(self):
      self.head = None

    def search(self,item):
      current = self.head
      while current is not None:
        if current.data == item:
          return True
        if current.data > item:
          return False
        current = current.next
      return False
    
    def add(self, item):
        current = self.head
        previous = None
        temp = Node(item)

        while current is not None and current.data < item:
            """The condition allows the iteration to continue as long as there are more nodes and the value in the current node is not larger than the item. """
            previous = current
            current = current.next
            """allow previous to follow one node behind current every time through the iteration"""

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

            