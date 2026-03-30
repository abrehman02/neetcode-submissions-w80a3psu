# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # to remove the node from the end of the linkedlist we can use
        # this 
        '''
        there are two methods 
        1 -
        the nth node from the end of linked list is the length - (n - 1) from the beginning

        to delete it 
        copy the next elements data into it 
        marked the next of current to next of next curr.next = temp.next 
        
        2 -
        place the second pointer to n from the beginning and 
        then start two pointer one at already at n and other at beginning 
        when the ahead pointer reaches the end the slow will be at the d position and 
        then delete it  
        '''

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        print("check ----->>> ",length)

        position = length - (n - 1)

        prev = None
        target = head
        counter = 1

        while target and counter < position :
            counter += 1
            prev = target
            target = target.next
        
        if target.next:
            temp = target.next
            target.val = temp.val
            target.next = temp.next
            temp.next = None
        else:
            if prev == None:
                return None
            prev.next = None 
        return head
