from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getNode(self, l: Optional[ListNode]) -> str:
        return f"{l.val}" + self.getNode(l.next) if l else ""
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # convert linked list to number
        l1_num = int(self.getNode(l1)[::-1])
        l2_num = int(self.getNode(l2)[::-1])

        # add two numbers
        add_rst = str(l1_num + l2_num)
        
        result = None
        # convert number to linked list
        for i in add_rst:
            result = ListNode(i, result)

        return result