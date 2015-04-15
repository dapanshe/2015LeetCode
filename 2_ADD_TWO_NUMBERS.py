# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        isAddOne = False
        dummy = ListNode(0)
        pre = dummy
        while (l1 is not None) and (l2 is not None):
            localSum = 0
            localSum = l1.val + l2.val + (isAddOne == True)
            if localSum >= 10:
                isAddOne = True
                localSum -= 10
            else:
                isAddOne = False
            newNode = ListNode(localSum)
            pre.next= newNode
            pre = newNode
            l1 = l1.next
            l2 = l2.next
        l = l1
        if l2 is not None:
            l = l2
        while l is not None:
            localSum = 0
            localSum = l.val + (isAddOne == True)
            if localSum >= 10:
                isAddOne = True
                localSum -= 10
            else:
                isAddOne = False
            newNode = ListNode(localSum)
            pre.next= newNode
            pre = newNode
            l = l.next
        if isAddOne:
            pre.next = ListNode(1)
        return dummy.next
