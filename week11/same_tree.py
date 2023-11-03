# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true


# def same_tree(p, q):

#     if len(p) != len(q):
#         print(False)
#     else:
#         for e in range(len(p)):
#             if p[e] == q[e]:
#                 print(f"elements at index {e} are the same: {p[e]}")
#             else:
#                 print(
#                     f"elements at index {e} are different: {p[e]} and {q[e]}")


# print(same_tr
# ee([1, 2, 3], [1, 2, 4]))

# Notes:
# Check the base case: if both trees are null, return true.
# Check if only one tree is null or the values of the current nodes are different, return false.
# Recursively check if the left subtrees of both trees are identical.
# Recursively check if the right subtrees of both trees are identical.
# Return the logical AND of the results from steps 3 and 4.


class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p is None or q is None:
            # print(p)
            # print(q)
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Construct binary trees
# p = TreeNode(1, TreeNode(2), TreeNode(3))
# q = TreeNode(1, TreeNode(2), TreeNode(3))

# # Check if the trees are the same using the Solution method
# result = Solution.isSameTree(p, q)
# print(result)

# issue with LeetCode and test cases. This passes test cases, but in VSC I need to construct the binary tree

# In this code, we define a TreeNode class and an isSymmetric function. The isMirror function checks if two trees are mirror images of each other, and the main isSymmetric function checks if the root of the binary tree is symmetric by calling isMirror for its left and right subtrees. If the binary tree is symmetric, the function returns True; otherwise, it returns False.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# check if left is empty and right is empty, which means there identical, return True
# if one is empty and not the other return False
# This line checks if the values of the left and right nodes are equal. If they are, it recursively calls isMirror for the left and right subtrees of left and the right and left subtrees of right. This recursive approach ensures that the entire tree is checked for symmetry by comparing each pair of nodes at the same level


def isSymmetric(root):
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

# if the tree itself is empty, its considered symmetric
    if not root:
        return True

    return self.isMirror(root.left, root.right)


# Example usage:
# Construct a symmetric binary tree
symmetric_tree = TreeNode(1, TreeNode(2, TreeNode(
    3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))


# Check if the tree is symmetric
result = isSymmetric(symmetric_tree)
print(result)  # This should print True

# Construct a non-symmetric binary tree
non_symmetric_tree = TreeNode(1, TreeNode(
    2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))

# Check if the tree is symmetric
result = isSymmetric(non_symmetric_tree)
print(result)  # This should print False
