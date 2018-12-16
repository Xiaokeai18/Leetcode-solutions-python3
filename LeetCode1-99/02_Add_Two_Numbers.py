# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        opt = l1
        plus = 0
        l1.val = l1.val + l2.val +plus
        
        if l1.val > 9:
            l1.val -= 10
            plus = 1
        else:
            plus = 0

        while l1.next and l2.next:
            l1,l2 = l1.next,l2.next
            l1.val = l1.val + l2.val +plus
            if l1.val > 9:
                l1.val -= 10
                plus = 1
            else:
                plus = 0
            
        while l1.next:
            l1= l1.next            
            l1.val += plus
            if l1.val > 9:
                l1.val -= 10
                plus = 1
            else:
                plus = 0

        while l2.next:
            l2 = l2.next            
            l1.next = ListNode(1)
            l1 = l1.next
            l1.val = l2.val + plus
            if l1.val > 9:
                l1.val -= 10
                plus = 1
            else:
                plus = 0

        if plus == 1:
            l1.next = ListNode(1)
        return opt