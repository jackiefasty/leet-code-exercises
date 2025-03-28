# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(head):
            prev = None
            curr = head

            while curr is not None:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode

            return prev
        
        def trimLeadingZeros(head):
            res = None
            curr = None
            carry = 0

            num1 = trimLeadingZeros(num1)
            num2 = trimLeadingZeros(num2)

            num1 = reverseZeros(num1) # type: ignore
            num2 = reverseZeros(num2) # type: ignore

            while num1 is not None or num2 is not None or carry != 0:
                sumValue = carry

                if num1 is not None:
                    sumValue += num1.data
                    num1 = num1.next

                if num2 is not None:
                    sumValue += num2.data

        