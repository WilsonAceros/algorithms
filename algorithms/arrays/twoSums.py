'''
    Leetcode: Two sum
    https://leetcode.com/problems/two-sum/
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = 0
        find = {}
        for i, j in enumerate(nums):
            sum = target - j
            if sum in find:
                return [find[sum], i]
            find[j] = i
