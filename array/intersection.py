'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        d1 = {x:nums1.count(x) for x in nums1}
        d2 = {x:nums2.count(x) for x in nums2}
        for i in d1:
          for x in range(min(d1.get(i, 0), d2.get(i, 0))):
            result.append(i)
        return result
