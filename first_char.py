'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = 0
        for i in s:
            if s.count(i) == 1:
                return c
            c = c + 1
        return -1
