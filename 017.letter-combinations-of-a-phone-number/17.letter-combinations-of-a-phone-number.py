#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (40.58%)
# Total Accepted:    368.7K
# Total Submissions: 899.2K
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution(object):
    def combinationTwo(self,l,digit):
        """
        :type l:list
        :type digit:str
        :rtype list
        """
        return [s+i for s in l for i in self.d[digit]]


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]        
        """
        self.d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if not digits:
            return []
        l1=list(self.d[digits[0]])
        digits=digits[1:]
        if not digits:
            return l1
        for i in digits:
            l1=self.combinationTwo(l1,i)
        return l1
if __name__ == "__main__":
    s=Solution()
    print(s.letterCombinations(''))

