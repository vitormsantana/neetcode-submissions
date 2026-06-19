# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def print_linked_list(head: ListNode) -> None:
            curr = head
            while curr:
                print(curr.val, end=" -> ")
                curr = curr.next
            print("None")

        while len(lists) > 1:
            dummy_0 = ListNode(val=0, next=lists[0])
            dummy_1 = ListNode(val=0, next=lists[1])
            dummy_ordered = ListNode(0)
            dummy_ordered_prev = ListNode(0, next=dummy_ordered)

            curr_0, curr_1 = lists[0], lists[1]

            while curr_0 is not None and curr_1 is not None:
                if curr_0.val > curr_1.val:
                    dummy_ordered.next = curr_1
                    dummy_ordered = dummy_ordered.next
                    curr_1 = curr_1.next
                else:
                    dummy_ordered.next = curr_0
                    dummy_ordered = dummy_ordered.next
                    curr_0 = curr_0.next

            while curr_0 is not None:
                dummy_ordered.next = curr_0
                dummy_ordered = dummy_ordered.next
                curr_0 = curr_0.next
            
            while curr_1 is not None:
                dummy_ordered.next = curr_1
                dummy_ordered = dummy_ordered.next
                curr_1 = curr_1.next

            lists[1] = dummy_ordered_prev.next.next
            lists = lists[1:]
                            
            #print_linked_list(dummy_ordered_prev.next.next)
        
        return lists[0] if lists else None
                