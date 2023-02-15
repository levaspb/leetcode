'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Results:
    Runtime: 31 ms
    Memory Usage: 13.9 MB
    Beats 92% of python3 submissions
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None: return None
        elif list2 is None: return list1
        elif list1 is None: return list2
        if list1.val > list2.val:
            start = result = list2
            cont = list1
        else:
            start = result = list1
            cont = list2
        current = start.val
        while True:
            if start.next == None:
                start.next = cont
                return result
            if start.next.val < cont.val:
                start = start.next
                continue
            current = start.val
            start_rest = start.next
            start.next = cont
            start = start.next
            cont = start_rest
