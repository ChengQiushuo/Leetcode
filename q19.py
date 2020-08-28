# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        c = head
        li = []
        while c!=None:
            li.append(c)
            c= c.next
        l = len(li)
        if l ==n:
            head = head.next
            return head
        if n == 1:
            li[l-2].next = None
            return head
        li[l-n-1].next = li[l-n+1]
        return head
