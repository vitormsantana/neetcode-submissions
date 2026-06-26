# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # [9, 9, 9] + [1, 1]

        # reverse_L1 = self.reverseLL(l1)
        # reverse_L2 = self.reverseLL(l2)

        reverse_L1 = l1
        reverse_L2 = l2

        dummy = ListNode(0)
        curr = dummy
        resto = 0

        while reverse_L1 and reverse_L2:
            summ = reverse_L1.val + reverse_L2.val
            if resto > 0:
                summ += resto
                resto = 0

            if len(str(summ)) > 1:
                curr.next = ListNode(int(str(summ)[1]))
                resto = 1
            
            else:
                curr.next = ListNode(summ)
            curr = curr.next
            reverse_L1 = reverse_L1.next
            reverse_L2 = reverse_L2.next
            if resto > 0 and not reverse_L1 and not reverse_L2:
                curr.next = ListNode(resto)

        if reverse_L1 or reverse_L2:
            while reverse_L1:
                summ = reverse_L1.val
                if resto > 0:
                    summ = reverse_L1.val + resto
                    resto = 0
                
                if len(str(summ)) > 1:
                    curr.next = ListNode(int(str(summ)[1]))
                    resto = 1
                else:
                    curr.next = ListNode(summ)
                curr = curr.next
                if not reverse_L1.next and resto > 0:
                    curr.next = ListNode(resto)
                reverse_L1 = reverse_L1.next
            
            while reverse_L2:
                summ = reverse_L2.val
                if resto > 0:
                    summ = reverse_L2.val + resto
                    resto = 0
                
                if len(str(summ)) > 1:
                    curr.next = ListNode(int(str(summ)[1]))
                    resto = 1
                else:
                    curr.next = ListNode(summ)
                curr = curr.next
                if not reverse_L2.next and resto > 0:
                    curr.next = ListNode(resto)
                reverse_L2 = reverse_L2.next

        # reverseFinal = self.reverseLL(dummy.next)
        reverseFinal = dummy.next

        return reverseFinal

    def reverseLL(self, head):

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev