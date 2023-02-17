'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Results:
    Runtime: 32 ms
    Memory Usage: 13.9 MB
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        def recursive_search(minimum: int, maximum: int):
            mediana = (maximum + minimum)//2
            if mediana == minimum:
                if isBadVersion(mediana):
                    return mediana
                else:
                    return maximum
            if isBadVersion(mediana):
                return recursive_search(minimum, mediana)
            else:
                return recursive_search(mediana+1, maximum)
            
        
        if n == 1:
            return n
        
        return recursive_search(1, n)
