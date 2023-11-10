# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: 3


# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


def maxDepth(self, root):
    if not root:
        return 0

    # left_depth = maxDepth(root.left)
    # right_depth = maxDepth(root.right)

    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
