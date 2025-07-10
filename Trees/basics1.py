# Edge	        The connection between two nodes.
# Depth	        Distance (# of edges) from root to a node.
# Height	    Distance (# of edges) from a node to its farthest leaf.
# Level	        Depth + 1. Root is at level 1.
# Subtree	    A tree formed from any node as root and all its descendants.
# Ancestor	    Any node on the path from a node to the root.
# Descendant	Any node reachable from a node downward.

#        1     Root is at level 1
#       /
#      2
#     /
#    3         Now for this 3, Depth is 2, level is 3, as depth is no. of edges from root to a node.

# NOW pay attention: Height is no. of edges from a node to its farthest leaf.
# So for this tree height is 2

# Some Tree to experiment
    #     1               <-- Level 1
    #    / \
    #   2   3             <-- Level 2
    #  /   / \
    # 4   5   6           <-- Level 3
    #      \
    #       7            <-- Level 4

# Tree Traversal
# DFS: InOrder, PreOrder, PostOrder
# BFS: Level order traverse


# Morris Traversal (Inorder/Preorder without recursion or stack)
# Space-efficient: O(1) space, modifies tree structure temporarily.
# Advanced, rarely asked in interviews unless you're going for a very senior role or optimization-specific problem.

# 💯💯
# Validate BST: This problem seems easy but a bit tricky 😳: https://leetcode.com/problems/validate-binary-search-tree/submissions/1648180394/

# 😎😎
# Convert BST to Sorted Doubly Linked List (In-place)

# 😎😎
# Trim a BST (Keep Nodes within Range)

# 😎😎
# Lowest Common Ancestor (LCA) in a BST

# 😎😎
# Smallest distance between 2 nodes of a Binary tree
# Find LCA and then sum distance of LCA from Each node ✅



from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Creating nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)


def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def preorder(root):
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


def level_order_traverse(root):
    queue = deque()
    if root:
        queue.appendleft(root)
    traversal = []
    while queue:
        node = queue.pop()
        traversal.append(node.val)
        if node.left:
            queue.appendleft(node.left)
        if node.right:
            queue.appendleft(node.right)
    return traversal


def height(root):
    if not root: return 0
    lh = 0
    if root.left:
        lh = height(root.left)
    rh = 0
    if root.right:
        rh = height(root.right)
    return 1 + max(lh, rh)


def diameter(root):
    if not root: return 0, 0
    ldw, ldi = 0, 0
    rdw, rdi = 0, 0
    if root.left:
        ldw, ldi = diameter(root.left)
    if root.right:
        rdw, rdi = diameter(root.right)
    
    rt_dw = max(ldw, rdw)
    rt_di = 1 + ldi + rdi
    return rt_dw, rt_di


def display(root):
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)

def _display_aux(node):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    if node is None:
        return [], 0, 0, 0

    line = str(node.val)

    # No child
    if node.left is None and node.right is None:
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child
    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child
    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = str(node.val)
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = str(node.val)
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [' ' * n] * (q - p)
    elif q < p:
        right += [' ' * m] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first + u * ' ' + second for first, second in zipped_lines]
    return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2


def serialize_tree(root):
    if not root:
        return "X"
    return f"{root.val} {serialize_tree(root.left)} {serialize_tree(root.right)}"


