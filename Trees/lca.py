from .basics1 import height, Node


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Build a binary tree with 4 levels
#            1
#         /     \
#       2         3
#     /   \     /   \
#    4     5   6     7
#   / \   / \
#  8  9 10  11


def build_tree():
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)

    return root



def lca(root, n1, n2):

    def path_fun(root, node, path):
        if root == None:
            return None
        if root.val == node.val:
            path.append(node.val)
            return path
        newPath = path + [root.val]
        path = path_fun(root.left, node, newPath)
        if path:
            return path
        path = path_fun(root.right, node, newPath)
        if path:
            return path
        return None

    p1 = path_fun(root, n1, [])
    p2 = path_fun(root, n2, [])

    # if p1 and p2:
    #     smallerLen = min(len(p1), len(p2))
    #     for i in ra
    # else:
    #     return None





r1 = build_tree()

lca(r1, Node(9), Node(11))

# print(p1)