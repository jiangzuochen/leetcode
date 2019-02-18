#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.92%)
# Total Accepted:    402.6K
# Total Submissions: 1.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        number=0
        while True:
            if len(strs)==0:
                return ''
            for s in strs:
                if len(s)==0:
                    return ''
                if number >= len(s):
                    return strs[0][0:number]
                if s[number] != strs[0][number]:
                    return strs[0][0:number]
            number+=1 
