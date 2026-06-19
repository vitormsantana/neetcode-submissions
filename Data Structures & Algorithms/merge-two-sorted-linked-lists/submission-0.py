# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        while list1 and list2:
            if list1.val >= list2.val:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next
            else:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
                
        if list1:
            while list1:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next

        if list2:
            while list2:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next

        return head.next