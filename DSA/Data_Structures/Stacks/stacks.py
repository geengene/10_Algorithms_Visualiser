    # empty() – Returns whether the stack is empty – Time Complexity: O(1)
    # size() – Returns the size of the stack – Time Complexity: O(1)
    # top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
    # push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
    # pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)
    
    

def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False

    return s.is_empty()

def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))





def binary_converter(decimal_num):
    rem_stack = []

    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.append(rem)
        decimal_num = decimal_num // 2

    bin_string = ""
    while not len(rem_stack)==0:
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string

print(binary_converter(42))
print(binary_converter(31))


def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decimal_num > 0: 
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string

print(base_converter(25, 2))
print(base_converter(25, 16))
print(base_converter(42, 15))


"""Implementing recursions as a Stack frame"""
def to_string(n, base):
    r_stack = Stack()
    convert_string = "0123456789ABCDEF"
    while n>0:
        if n<base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n%base])
        n = n//base
    
    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())

    return res

print(to_string(1453, 16))

