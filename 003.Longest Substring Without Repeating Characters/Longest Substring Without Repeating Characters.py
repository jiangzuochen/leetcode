class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        j=0
        dict={}
        max = 0 
        for char in s:
            j+=1
            if char not in dict:
                dict[char]=j
                if max < j - i:
                    max = j-i
            else:
                if dict[char] > i:
                    i = dict[char]
                dict[char] = j
                if max < j - i:
                    max = j-i
        return max