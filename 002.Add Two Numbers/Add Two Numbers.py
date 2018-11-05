# Definition for singly-linked list.
# class ListNode:
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
        str1=''
        str2=''
        while l1 is not None or l2 is not None:
            if l1 != None:
                str1=str(l1.val)+str1
                l1=l1.next
            if l2 != None:
                str2=str(l2.val)+str2
                l2=l2.next
        l3=resultList=ListNode(None)
        for y in str(int(str1)+int(str2))[::-1]:
                if l3.val is None:
                      l3.val = int(y)
                else:
                      l3.next = ListNode(int(y))
                      l3 = l3.next
        return resultList