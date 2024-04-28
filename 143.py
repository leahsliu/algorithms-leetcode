# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        res = []
        inOrder = []
        while head:
            inOrder.append(head.val)
            head = head.next

        l,r = 0, len(inOrder)-1
        while l < r:
            res += [inOrder[l], inOrder[r]]
            l += 1
            r -= 1
        
        # case where linked list has odd number of nodes
        if l == r:
            res += [inOrder[l]]
        return res

n0 = ListNode(val=4, next=None)

n1 = ListNode(val=3, next=n0)
n2 = ListNode(val=2, next=n1)
n3 = ListNode(val=1, next=n2)

s = Solution()
print("sol: [1,4,2,3] res: ", s.reorderList(n3))

n0 = ListNode(val=5, next=None)
n1 = ListNode(val=4, next=n0)
n2 = ListNode(val=3, next=n1)
n3 = ListNode(val=2, next=n2)
n4 = ListNode(val=1, next=n3)
print("sol: [1,5,2,4,3] res: ", s.reorderList(n4))

print("sol: [5] res: ", s.reorderList(n0))
