
# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0) # Create temporary node
        temp.next = head # Set temp node as new head
        prev = temp # Set previous to temp
        curr = head # Set current to head

        # Traverse Linked List with a while loop
        while curr:
            if curr.val == val: # Check if the current value matches the target value
                prev.next = curr.next # Remove target value node by updating next pointer to point to the node that comes after current
            else:
                prev = curr # prev is updated to curr to ensure prev refers to the node before curr
            curr = curr.next
        
        return temp.next