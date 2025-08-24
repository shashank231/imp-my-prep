
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_nodes(root):
    """Helper to count actual nodes in the tree"""
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def isCBT(root, index, cnt):
    # If tree is empty
    if root is None:
        return True
    
    # If index assigned to node is out of range
    if index >= cnt:
        return False
    
    # Recurse for left and right subtrees
    left  = isCBT(root.left,  2 * index + 1, cnt)
    right = isCBT(root.right, 2 * index + 2, cnt)
    
    return left and right

# Build the tree: 
#        1
#       / \
#      2   3
root = Node(1)
root.left = Node(2)
root.right = Node(3)

cnt = count_nodes(root)
print(isCBT(root, 0, cnt))  # ✅ True
