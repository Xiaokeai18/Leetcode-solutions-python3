# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        p = dummy
        while p.next and p.next.next:
            node1 = p.next
            node2 = node1.next 
            node_tmp = node2.next
            node2.next = node1
            node1.next = node_tmp

            p.next = node2
            p = node1
            
        return dummy.next