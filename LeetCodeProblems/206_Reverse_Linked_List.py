# 206. Reverse Linked List

# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.

# Tightly-coupled solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

