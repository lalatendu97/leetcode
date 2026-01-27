# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        lst = []
        while head.next:
            lst.append(head.val)
            head = head.next
        lst.append(head.val)

        idx = []
        for i in nums:
            idx.append(lst.index(i))
        idx.sort()

        res = len(idx)
        for i in range(1, res):
            if idx[i - 1] + 1 == idx[i]:
                res -= 1

        return res