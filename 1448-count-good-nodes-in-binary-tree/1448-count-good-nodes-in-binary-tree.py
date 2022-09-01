class Solution:
    def goodNodes(self, root: TreeNode, curMax = -math.inf) -> int:
        if root == None: return 0
        return (curMax <= root.val) + self.goodNodes(root.left, max(curMax, root.val)) + self.goodNodes(root.right, max(curMax, root.val))