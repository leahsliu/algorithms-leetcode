# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = [(0, root)]
        cols = {}
        for x, node in q:
            if node:
                left = x-1, node.left
                right = x+1, node.right
                q += left, right

                if x not in cols:
                    cols[x] = []
                cols[x].append(node.val)

        return [cols[x] for x in sorted(cols)]








s = Solution()
t = TreeNode(val=4, left=None, right=None)
t1 = TreeNode(val=0, left=None, right=None)
t2 = TreeNode(val=9, left=t, right=t1)
t3 = TreeNode(val=1, left=None, right=None)
t4 = TreeNode(val=7, left=None, right=None)
t5 = TreeNode(val=8, left=t3, right=t4)
t6 = TreeNode(val=3, left=t2, right=t5)



print("soln: [[4], [9], [3, 0, 1], [8], [7]] \nres: ", s.verticalOrder(t6))





        
        # cols = defaultdict(list)

        # queue = [(root,0)]

        # for node,i in queue:
        #     if node:
        #         cols[i].append(node.val)
        #         queue += (node.left, i-1), (node.right, i+1)
        # return [cols[i] for i in sorted(cols)]