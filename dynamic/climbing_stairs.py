'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:
1 <= n <= 45
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        array = [1,2,3]
        if n == 1 or n == 2 or n == 3:
            return n
        for i in range(3, n):
            result = array[i-1] + array[i-2]
            array.append(result)
        return array[-1]
