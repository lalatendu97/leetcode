# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        idx = [0 for _ in range(len(nums))]
        i = 0

        while head.next:
            if head.val in nums:
                idx[nums.index(head.val)] = i
            i += 1
            head = head.next

        if head.val in nums:
            idx[nums.index(head.val)] = i

        idx.sort()
        res = len(idx)
        for i in range(1, res):
            if idx[i - 1] + 1 == idx[i]:
                res -= 1

        return res