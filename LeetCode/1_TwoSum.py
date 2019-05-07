'''1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Input: Given nums = [2, 7, 11, 15], target = 9,
Output: Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
'''

"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if ((nums[i] + nums[j]) == target):
                    return [i, j]
