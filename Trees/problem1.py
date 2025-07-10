# TREE
# Level 1:        1
#                / \
# Level 2:     2     3
#             /     / \
# Level 3:   4     5   6
#           /       \    \
# Level 4: 7         8    9
#             \            \
# Level 5:     10           11
#             /               \
# Level 6:   12               13
#           /                   \
# Level 7: 14                   15
#                                  \
# Level 8:                         16

from collections import deque
from .basics1 import height, Node

nodes = {i: Node(i) for i in range(1, 17)}
# Manually linking nodes to form the desired tree
root = nodes[1]
root.left = nodes[2]
root.right = nodes[3]
nodes[2].left = nodes[4]
nodes[3].left = nodes[5]
nodes[3].right = nodes[6]
nodes[4].left = nodes[7]
nodes[5].right = nodes[8]
nodes[6].right = nodes[9]
nodes[7].right = nodes[10]
nodes[8].left = nodes[12]
nodes[9].right = nodes[11]
nodes[10].left = nodes[12]

nodes[11].right = nodes[13]
nodes[12].left = nodes[14]
nodes[13].right = nodes[15]
nodes[15].right = nodes[16]

def left_view(root):
    if not root: return
    queue = deque()
    queue.append(root)
    left_view = []

    while (queue):
        node = queue.pop()
        if node.left:
            queue.appendleft(node.left)
        else:
            if node.right:
                queue.appendleft(node.right)
        left_view.append(node.val)
    
    print(left_view)


def diameter(root):
    """
    You're recursively computing the diameter and then calling height() on the same subtrees again.
    That means the same subtrees are traversed multiple times, especially in large trees.
    """
    if not root:
        return 0
    left = diameter(root.left)
    right = diameter(root.right)
    left_height = height(root.left)
    right_height = height(root.right)
    return max(
        1 + left_height + right_height,
        left, 
        right,
    )


def diameter2(root):
    """
    memoization can help avoid redundant height() calls by caching results per node,
    and since nodes may have the same values, you should cache by node identity, not by value.
    """
    height_cache = {}

    def height(node):
        if not node:
            return 0
        if node in height_cache:
            return height_cache[node]

        h = 1 + max(height(node.left), height(node.right))
        height_cache[node] = h
        return h

    def compute_diameter(node):
        if not node:
            return 0

        left_diameter = compute_diameter(node.left)
        right_diameter = compute_diameter(node.right)

        left_height = height(node.left)
        right_height = height(node.right)

        current_diameter = left_height + right_height  # edges

        return max(current_diameter, left_diameter, right_diameter)

    return compute_diameter(root)


def diameter3(node):
    """
    Time complexity: O(n)
    Space complexity: O(h) for recursion stack
    Fast, clean, and elegant
    Doesn't require any caching
    """
    if not node:
        return 0, 0  # height, diameter
    lh, ld = diameter3(node.left)
    rh, rd = diameter3(node.right)

    height = 1 + max(lh, rh)
    diameter_through_node = lh + rh
    max_diameter = max(ld, rd, diameter_through_node)
    return height, max_diameter


def lowest_common_ancestor(root, p, q):
    """
    LCA of p and q
    """
    if not root:
        return root
    if root==p or root==q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    
    return left if left else right


def check_identical(root1, root2):
    if not root1 and not root2:
        return True

    if root1 and not root2:
        return False

    if root2 and not root1:
        return False

    if root1.val != root2.val:
        return False
    
    left = check_identical(root1.left, root2.left)
    right = check_identical(root1.right, root2.right)

    if left and right:
        return True
    return False

