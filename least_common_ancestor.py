class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    
    def find_min_binary_tree(self, root, p, q):
        if not root:
            return False

        left_side = self.find_min_binary_tree(root.left, p, q)
        right_side = self.find_min_binary_tree(root.right, p, q)
 
        if (root.val == p or root.val == q) + left_side + right_side == 2: 
            self.ans = root
        return (root.val == p or root.val == q) or left_side or right_side

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.find_min_binary_tree(root, p.val, q.val)
        return self.ans
