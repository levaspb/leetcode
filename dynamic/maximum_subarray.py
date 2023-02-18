'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        vrednost = []
        vrednost.append(nums[0])
        
        for i in nums[1:]:
            if vrednost[-1] < 0:
                result = i
            else:
                result = i + vrednost[-1]
            vrednost.append(result)
        print(vrednost)
        result = max(vrednost)
        
        return result
