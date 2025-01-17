# The basic building block for the linked list implementation is the node. Each node object must hold at least two pieces of information. First, the node must contain the list item itself. We will call this the data field of the node. In addition, each node must hold a reference to the next node.

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
    
class UnorderedList:
  
  def __init__(self):
    """Contructing a list has no value. the special reference None will again be used to state that the head of the list does not refer to anything. It refers to the next node of the list which contains the first item of the list. In turn, that node holds a reference to the next node (the next item), and so on. It is very important to note that the list class itself does not contain any node objects. Instead it contains a single reference to only the first node in the linked structure."""
    self.head = None 

  def is_empty(self):
    """checks to see if the head of the list is a reference to None. The result of the boolean expression self.head == None will only be true if there are no nodes in the linked list. """
    return self.head == None
  
  def add(self, item):
    """creates a new node and places the item as its data. """
    temp = Node(item)
    """changes the next reference of the new node to refer to the old first node of the list."""
    temp.set_next(self.head)
    """modify the head of the list to refer to the new node."""
    self.head = temp

  def size(self): #traverse the linked list and keep a count of the number of nodes that occurred.
    """external reference is called current and is initialized to the head of the list"""
    current = self.head
    count = 0
    while current is not None:
        """As long as the current reference has not seen the end of the list (None), we move current along to the next node via the assignment statement """
        count = count + 1
        current = current.next
    return count
  
  def search(self, item):
    current = self.head
    while current is not None:
        if current.data == item:
            return True
        current = current.next
    return False
  
  def remove(self, item):
    """assign initial values to the two references. Note that current starts out at the list head as in the other traversal examples."""
    current = self.head
    """previous, however, is assumed to always travel one node behind current. For this reason, previous starts out with a value of None since there is no node before the head """
    previous = None

    while current is not None:
        if current.data == item:
            break
        """previous must first be moved one node ahead to the location of current. At that point, current can be moved. This process is often referred to as inchworming, as previous must catch up to current before current moves ahead"""
        previous = current
        current = current.next


    if current is None:
      raise ValueError("{} is not in the list".format(item))

    if previous is None:
      """If previous did not move, it will still have the value None when the loop breaks. the head of the list is modified to refer to the node after the current node, in effect removing the first node from the linked list."""
      self.head = current.next

    else:
        previous.next = current.next



"""append, insert, index, and pop are left as exercises. Remember that each of these must take into account whether the change is taking place at the head of the list or someplace else. Also, insert, index, and pop require that we name the positions of the list. We will assume that position names are integers starting with 0."""