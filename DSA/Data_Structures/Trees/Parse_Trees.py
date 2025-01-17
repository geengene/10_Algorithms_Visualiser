# Rules: 
# 1. If the current token is a "(", add a new node as the left child of the current node, and descend to the left child.
# 2. If the current token is in the list ["+", "-", "/", "*"], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.
# 3. If the current token is a number, set the root value of the current node to the number and return to the parent.
# 4. If the current token is a ")", go to the parent of the current node.

# (3+(4*5))

# Create an empty tree.

# Read ( as the first token. By rule 1, create a new node as the left child of the root. Make the current node this new child.

# Read 3 as the next token. By rule 3, set the root value of the current node to 3 and go back up the tree to the parent.

# Read + as the next token. By rule 2, set the root value of the current node to + and add a new node as the right child. The new right child becomes the current node.

# Read ( as the next token. By rule 1, create a new node as the left child of the current node. The new left child becomes the current node.

# Read 4 as the next token. By rule 3, set the value of the current node to 4. Make the parent of 4 the current node.

# Read * as the next token. By rule 2, set the root value of the current node to * and create a new right child. The new right child becomes the current node.

# Read 5 as the next token. By rule 3, set the root value of the current node to 5. Make the parent of 5 the current node.

# Read ) as the next token. By rule 4 we make the parent of * the current node.

# Read ) as the next token. By rule 4 we make the parent of + the current node. At this point there is no parent for +, so we are done.

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
    
class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child

    def get_root_val(self):
        return self.key

    def set_root_val(self, new_obj):
        self.key = new_obj

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child
    
    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)

def build_parse_tree(fp_expr):
    fp_list = fp_expr.split()
    p_stack = Stack() # A simple solution to keeping track of parents as we traverse the tree is to use a stack. Whenever we want to descend to a child of the current node, we first push the current node on the stack. When we want to return to the parent of the current node, we pop the parent off the stack.
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.left_child
        elif i in ["+", "-", "*", "/"]:
            current_tree.root = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.right_child
        elif i.isdigit():
              current_tree.root = int(i)
              parent = p_stack.pop()
              current_tree = parent
        elif i == ")":
              current_tree = p_stack.pop()
        else:
              raise ValueError(f"Unknown operator '{i}'")

    return expr_tree



pt = build_parse_tree("( ( 12 - 5 ) / 3 )")


import operator

def evaluate(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    left_child = parse_tree.left_child
    right_child = parse_tree.right_child

    if left_child and right_child:
        fn = operators[parse_tree.root]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.root
    
print(evaluate(pt))

# Tree Traversals
# Preorder
#     In a preorder traversal, we visit the root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree.

# Inorder
#     In an inorder traversal, we recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree.

# Postorder
#     In a postorder traversal, we recursively do a postorder traversal of the left subtree and the right subtree followed by a visit to the root node.


def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)

def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)

def inorder(tree):
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)

def postordereval(tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    result_1 = None
    result_2 = None
    if tree:
        result_1 = postordereval(tree.left_child)
        result_2 = postordereval(tree.right_child)
        if result_1 and result_2:
            return operators[tree.key](result_1, result_2)
        return tree.key
    
def print_exp(tree):
    result = ""
    if tree:
        result = "(" + print_exp(tree.left_child)
        result = result + str(tree.key)
        result = result + print_exp(tree.right_child) + ")"
    return result