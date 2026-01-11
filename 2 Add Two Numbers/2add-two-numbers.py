# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def func1(l):
            if l.next == None:
                return l.val
            return l.val + func1(l.next) * 10 

        def func2(val):
            if val:
                return ListNode(val = val % 10, next = func2(val // 10))
            return None
        
        l1 = func2(func1(l1) + func1(l2))
        return l1 if l1 else ListNode(val=0)
            
