

    #        8
    #      /   \
    #     3     10
    #    / \      \
    #   1   6      14
    #      / \     /
    #     4   7   13


from .basics1 import Node, display, serialize_tree


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)


def searchBST(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)


def inorder(root):
    """
    Inorder of BST gives the sorted version of BST. 
    """
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


def insertIntoBST(root, val):
    if not root:
        return Node(val)
    
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)

    return root


def searchNumAndParentInBST(root, num):
    """
    return Node(num), Node(num_parent)
    """
    if not root:
        return None, None

    if root.val == num:
        return root, None

    if root.left and root.left.val == num:
        return root.left, root
    if root.right and root.right.val == num:
        return root.right, root
    
    nd, nd_parent = None, None
    nd, nd_parent = searchNumAndParentInBST(root.left, num)
    if not nd:
        nd, nd_parent = searchNumAndParentInBST(root.right, num)
    return nd, nd_parent


def deleteNode(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Case 1 & 2: Node with only 1 child or no child
        if not root.left:
            return root.right # agar nahi hai tab b handle ho gaya or hai to b ho gaya
        elif not root.right:
            return root.left
        
        # Case 3: Node with 2 children
        # Get the inorder successor (min in right subtree)
        min_larger_node = getMin(root.right)
        root.val = min_larger_node.val
        root.right = deleteNode(root.right, min_larger_node.val)
    
    return root

def getMin(node):
    while node.left:
        node = node.left
    return node


""" 😎😎😎😎 """
def kthSmallestElementinBST(root, k):
    """
    short circuiting is important here for optimized solution
    """
    count = k
    result = None

    def inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return
        inorder(node.left)
        count -= 1
        if count == 0:
            result = node.val
            return
        inorder(node.right)

    inorder(root)
    return result

