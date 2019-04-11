#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (41.39%)
# Total Accepted:    313.7K
# Total Submissions: 729.9K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length=len(nums)
        minValue=nums[0]+nums[1]+nums[2]-target
        for i in range(length-2):
            l=i+1
            r=length-1
            while l<r:
                value=nums[i]+nums[l]+nums[r]-target#使value逐渐靠近0
                if abs(minValue)>abs(value):
                    minValue = value
                if value >0:
                    r-=1
                    continue
                elif value <0:
                    l+=1
                    continue
                else:
                    return target
        return minValue+target
                
        

