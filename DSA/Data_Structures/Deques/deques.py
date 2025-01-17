#  A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue. It has two ends, a front and a rear, and the items remain positioned in the collection. What makes a deque different is the unrestrictive nature of adding and removing items. New items can be added at either the front or the rear. Likewise, existing items can be removed from either end. In a sense, this hybrid linear structure provides all the capabilities of stacks and queues in a single data structure.

class Deque:
    """Deque implementation as a list"""
    def __init__(self):
        """Create new deque"""
        self._items = []

    def is_empty(self):
        """Check if the deque is empty"""
        return not bool(self._items)

    def add_front(self, item):
        """Add an item to the front of the deque"""
        self._items.append(item)

    def add_rear(self, item):
        """Add an item to the rear of the deque"""
        self._items.insert(0, item)

    def remove_front(self):
        """Remove an item from the front of the deque"""
        return self._items.pop()

    def remove_rear(self):
        """Remove an item from the rear of the deque"""
        return self._items.pop(0)

    def size(self):
        """Get the number of items in the deque"""
        return len(self._items)
    
def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
