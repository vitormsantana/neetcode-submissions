# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rest = 0
        dummy = ListNode(0)
        pre_head = dummy
        curr_1 = l1
        curr_2 = l2
        flag = 0

        while curr_1 or curr_2:
            if curr_1 and curr_2:
                summ = curr_1.val + curr_2.val
                if summ >= 10:
                    rest = (summ + rest + flag) - 10
                    flag = 1

                    summ = 0
                    dummy.next = ListNode(rest)
                    rest = 0

                else:
                    summ = (summ + rest + flag)
                    if summ >= 10:
                        rest = (summ) - 10
                        flag = 1

                        summ = 0
                        dummy.next = ListNode(rest)
                        rest = 0
                    else:
                        flag = 0
                        dummy.next = ListNode(summ)

                dummy = dummy.next
                curr_1, curr_2 = curr_1.next, curr_2.next
            
            else:
                if curr_1:
                    while curr_1:
                        summ = curr_1.val + flag
                        if summ >= 10:
                            rest = (summ + rest) - 10
                            flag = 1

                            summ = 0
                            dummy.next = ListNode(rest)
                            rest = 0

                        else:
                            summ = (summ + rest)
                            flag = 0
                            dummy.next = ListNode(summ)

                        dummy = dummy.next
                        curr_1 = curr_1.next

                if curr_2:
                    while curr_2:
                        summ = curr_2.val + flag
                        if summ >= 10:
                            rest = (summ + rest) - 10
                            flag = 1

                            summ = 0
                            dummy.next = ListNode(rest)
                            rest = 0

                        else:
                            summ = (summ + rest)
                            flag = 0
                            dummy.next = ListNode(summ)

                        dummy = dummy.next
                        curr_2 = curr_2.next

            if flag == 1:
                dummy.next = ListNode(flag)

        return pre_head.next