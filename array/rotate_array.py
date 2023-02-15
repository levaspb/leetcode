'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = [nums[x] for x in range(-k, len(nums)-k)]
        
