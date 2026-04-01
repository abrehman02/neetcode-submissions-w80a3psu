# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # i will create a new ans ll

        ans = ListNode()
        curr = ans
        # prev = None
        # assuming these ll can be of different lengths
        carry = 0
        while l1 or l2 or carry :
            # if there is a carry at the last node then a new node will be needed
            value = carry
            if l1 :
                value += l1.val
                l1 = l1.next
            if l2 :
                value += l2.val
                l2 = l2.next
            
            # if value > 9 :
                # do the value carry logic
            carry = value // 10

            value = value % 10

            curr.val = value

            if l1 or l2 or carry:
                new = ListNode()
                curr.next  = new
                prev = curr
                curr = curr.next
        
        # prev.next = None

        return ans
                