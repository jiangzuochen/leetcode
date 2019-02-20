#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (30.47%)
# Total Accepted:    283K
# Total Submissions: 928.7K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
import math
class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if len(s)<3 or numRows < 2:
            return s
        i=0
        blockLen=numRows*2-2
        #numBlocks=len(s)//blockLen if len(s)%blockLen == 0 or len(s)//blockLen+1
        numBlocks=math.ceil(len(s)/blockLen)
        strs=['']*numRows
        while i<numBlocks:
            if i==numBlocks-1:
                block=s[blockLen*i:]
            else:
                block=s[blockLen*i:blockLen*i+blockLen]
            for j in range(numRows):
                if j<len(block):
                    strs[j]+=block[j]
                if blockLen-j<len(block) and j!=0 and j!=numRows-1:
                    strs[j]+=block[blockLen-j]
            i+=1
        return ''.join(strs)
if __name__ == "__main__":
    s=Solution()
    print(s.convert('PAYPALISHIRING',3))

                            