'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Results:
    Runtime: 197 ms
    Memory Usage: 18.3 MB
    Beats 82% of python3 submissions
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        lenght = len(s)
        for i in range(lenght//2):
            s[i], s[-i-1] = s[-i-1], s[i]
