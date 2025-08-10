from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Hitung kontribusi kiri & kanan, abaikan jika negatif
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Path yang melewati node ini
            current_path_sum = node.val + left_gain + right_gain
            
            # Update max_sum global
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return kontribusi ke atas
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum
