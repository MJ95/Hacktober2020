# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val==val:
            return root
        elif root.val>val and root.left!=None:
            return self.searchBST(root.left,val)
        elif root.val<val and root.right!=None:
            return self.searchBST(root.right,val)
            
    #function to check unique binary search tree   
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0]=dp[1] = 1
        for i in range(2,n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
                print(dp)
        return dp[n]
