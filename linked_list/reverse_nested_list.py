'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_begin = node_end = head
        topology = list()
        if head == None:
            return head
        while node_end.next != None:
            topology.append(node_end)
            node_end = node_end.next
        topology.append(node_end)
        depth = len(topology)
        for i in range(depth//2):
            nodeStart = topology[i]
            nodeEnd = topology[depth-i-1]
            nodeVal = nodeEnd.val
            nodeEnd.val = nodeStart.val
            nodeStart.val = nodeVal
        return head
