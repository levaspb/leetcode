'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
          d[num] = d.get(num, 0) + 1
        for num in nums:
          if d[num] == 1:
            return num
