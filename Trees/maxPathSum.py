

# def fun1(root):

#     maxa = float('-inf')

#     left_node_present, max_sum_left = fun1(root.left) if root.left else (False, 0)
#     right_node_present, max_sum_right = fun1(root.right) if root.right else (False, 0)

#     cand1 = root.val
#     cand2 = cand3 = cand4 = float('-inf')
#     root_preset_in_maxsum = False
    
#     if left_node_present:
#         cand2 = root.val + max_sum_left if (max_sum_left + root.val) > max_sum_left else max_sum_left
#     if right_node_present:
#         cand3 = root.val + max_sum_right if (max_sum_right + root.val) > max_sum_right else max_sum_right

#     if left_node_present and right_node_present:
#         cand4 = root.val + max_sum_left + max_sum_right
    
#     maxa = max(cand1, cand2, cand3, cand4)
#     if maxa == cand1:
#         root_preset_in_maxsum = True
#     elif maxa == cand2 and cand2 == root.val + max_sum_left:
#         root_preset_in_maxsum = True
#     elif maxa == cand3 and cand3 == root.val + max_sum_right:
#         root_preset_in_maxsum = True
#     elif maxa == cand4:
#         root_preset_in_maxsum = True

#     return root_preset_in_maxsum, maxa

class Solution:

    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            # Only consider positive contributions
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            # Path passing through this node
            local_max = node.val + left + right
            # Update global max path sum
            self.max_sum = max(self.max_sum, local_max)
            # Return path that can be extended to parent (only one side)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
