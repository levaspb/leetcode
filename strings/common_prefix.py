'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Results:
    Runtime: 33 ms
    Memory Usage: 14 MB
    Beats 80-90% of python3 submissions
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_len = len(strs)
        prefix = ''
        min_len = len(min(strs, key=len))
        for i in range(min_len):
            result = True
            for j in range(list_len - 1):
                if strs[j][i] != strs[j+1][i]:
                    result = False
                    break
            if not result: return prefix
            prefix = prefix + strs[0][i:i+1]
        return prefix
