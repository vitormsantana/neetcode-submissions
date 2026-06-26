# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        count = 0

        while curr:
            size += 1
            curr = curr.next
        
        if size == n:
            dummy = ListNode(0, head)
            dummy.next = head.next
            return dummy.next
            
        curr = head
        while curr:
            if count == size - n - 1:
                print(f'vai pular agora , count {count}')
                curr.next = curr.next.next
            count += 1
            curr = curr.next
        
        return head