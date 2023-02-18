'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
 

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.

Results:
    Runtime: 83 ms
    Memory Usage: 14 MB
    Beats 90% of python3 submission
'''

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = Counter(s)
        for c, i in enumerate(s):
            if char_dict[i] == 1:
                return c
        return -1
