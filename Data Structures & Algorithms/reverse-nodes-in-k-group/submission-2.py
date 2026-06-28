# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head

        listOfSeparatedHeads = self.separateFromLL(head, k)
        
        for node in listOfSeparatedHeads:
            self.printLL(node)

        for j in range(len(listOfSeparatedHeads)):
            if self.getSizeFromLL(listOfSeparatedHeads[j]) == k:
                separated = self.reverseLL(listOfSeparatedHeads[j])
                listOfSeparatedHeads[j] = separated
        
        for node in listOfSeparatedHeads:
            self.printLL(node)

        dummy = ListNode(0, listOfSeparatedHeads[0])
            
        for i in range(len(listOfSeparatedHeads)):
            if i < len(listOfSeparatedHeads) - 1:
                curr = listOfSeparatedHeads[i]
                while curr and curr.next:
                    curr = curr.next
                curr.next = listOfSeparatedHeads[i+1]
            else:
                curr = listOfSeparatedHeads[i]
                while curr and curr.next:
                    curr = curr.next
                curr.next = None
        return dummy.next

    def getSizeFromLL(self, head):
        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1
        
        return size
    
    def separateFromLL(self, head, k) -> Optional[[ListNode]]:
        size = self.getSizeFromLL(head)

        qtyOfSeparations = size // k
        if qtyOfSeparations == 0:
            return []

        array_of_heads = []
        curr = head
        countSeparations = 0
        countNodes = 1
        while curr and countSeparations <= qtyOfSeparations - 1:
            curr = curr.next
            countNodes += 1
            if countNodes == k:
                countSeparations += 1
                lastOfFirstPart = curr
                firstOfNextPart = curr.next
                lastOfFirstPart.next = None
                array_of_heads.append(head)
                head = firstOfNextPart
                curr = head
                countNodes = 1
        
        if curr:
            array_of_heads.append(curr)

        return array_of_heads

    def reverseLL(self, head):
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
    
    def printLL(self, head):
        curr = head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next

        print(values)