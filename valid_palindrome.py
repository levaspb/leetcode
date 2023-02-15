'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

Result:
    Runtime: 42 ms
    Memory Usage: 14.8 MB
    Beats 87% of python3 submissions

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = ''.join(c for c in s if c.isalnum())
        s_alnum = s_alnum.lower()
        lenght = len(s_alnum)
        for i in range(lenght//2):
            if s_alnum[i] != s_alnum[-i-1]:
                return False
        return True

