# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        for i in range(len(lists)):
            if i == 0:
                new_head = lists[i]
            else:
                new_head = self.mergeTwoLists(new_head, lists[i])

        return new_head
        
    def mergeTwoLists(self, head_1, head_2):
        if head_1.val <= head_2.val:
            dummy = ListNode(0, head_1)
        else: 
            dummy = ListNode(0, head_2)

        curr = dummy
        while head_1 and head_2:
            if head_1.val <= head_2.val:
                curr.next = head_1
                curr = curr.next
                head_1 = head_1.next
            else:
                curr.next = head_2
                curr = curr.next
                head_2 = head_2.next
        
        if head_1:
            curr.next = head_1
        if head_2:
            curr.next = head_2

        return dummy.next  
