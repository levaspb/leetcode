'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for x in nums:
          d[x] = d.get(x, 0) + 1
          if d[x] > 1: 
            return True
        return False
