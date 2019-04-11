#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.55%)
# Total Accepted:    500.5K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#三数和为0，必然有负有正，或全为0.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        S=[]
        nums.sort()
        length=len(nums)
        for i in range(length-2):
            if i >0:
                if nums[i]==nums[i-1]:#nums[i]去重
                    continue
            if nums[i]>0:
                break
            l=i+1
            r=length-1
            while l<r:
                if l!= i+1 and nums[l]==nums[l-1]:#nums[l]去重
                    l+=1
                    continue
                if r!= length-1 and nums[r]==nums[r+1]:#nums[r]去重
                    r-=1
                    continue
                value= nums[i]+nums[l]+nums[r]
                if value>0:
                    r-=1
                elif value < 0:
                    l+=1
                else:
                    S.append([nums[i],nums[l],nums[r]])#
                    r-=1
                    l+=1
        return S

if __name__ == "__main__":
    s=Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
    #print("你好")