class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            self.maxDiameter = max(self.maxDiameter, left + right)

            return 1 + max(left, right)

        height(root)
        return self.maxDiameter