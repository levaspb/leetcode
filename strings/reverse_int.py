'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        if x < 0:
            result = -int(s[::-1])
            if result < -2147483648: return 0
        else:
            result = int(s[::-1])
            if result > 2147483647: return 0
        return result

