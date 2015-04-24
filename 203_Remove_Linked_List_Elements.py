# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head == None:
            return None
        dummy = ListNode(0)
        pre = dummy
        curr = head
        while curr != None:
            if curr.val != val:
                pre.next = curr
                pre, curr = curr, curr.next
            else:
                curr = curr.next
        pre.next = None
        return dummy.next
        
