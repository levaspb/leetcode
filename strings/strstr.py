'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Results:
    Runtime: 24 ms
    Memory Usage: 13.9 MB
    Beats 96% of python3 submissions
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        if needle_len > haystack_len:
            return(-1)
        for i in range(haystack_len - needle_len + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i+needle_len] == needle:
                    return(i)
        return(-1)
