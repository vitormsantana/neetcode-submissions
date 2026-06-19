class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        qtd = 0
        temp = head
        while temp is not None:
            qtd += 1
            temp = temp.next

        index_to_remove = qtd - n

        if index_to_remove == 0:
            head = head.next
            return head
        
        cursor = head
        for _ in range(index_to_remove - 1):
            cursor = cursor.next
        cursor.next = cursor.next.next

        return head