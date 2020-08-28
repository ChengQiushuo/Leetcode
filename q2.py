# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = ListNode()
        head = sum
        c = 0
        while l1!=None and l2!= None:
            sum.next = ListNode((l1.val + l2.val+c)%10)
            if l1.val + l2.val+c>9:
                c = 1
            else:
                c = 0
            sum = sum.next
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            sum.next = ListNode((l1.val+c)%10)
            if l1.val +c>9:
                c = 1
            else:
                c = 0
            sum = sum.next
            l1 = l1.next
        while l2 != None:
            sum.next = ListNode((l2.val+c)%10)
            if l2.val +c>9:
                c = 1
            else:
                c = 0
            sum = sum.next
            l2 = l2.next
        if c !=0:
           sum.next = ListNode(1) 
        return head.next
