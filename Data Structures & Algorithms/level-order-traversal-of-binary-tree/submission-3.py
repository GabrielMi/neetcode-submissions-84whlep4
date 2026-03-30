# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            curr = [n for n in queue]
            subList = []
            while queue:
                subList.append(queue.pop(0).val)
            res.append(subList)
            for node in curr:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
