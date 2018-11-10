class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen=1
        dict={}
        length=len(s)
        start=0
        for i in range(length):
            for j in range(i+1):
                if i-j <2:
                    dict[(i,j)]=(s[i]==s[j])
                else:
                    dict[(i,j)]=((s[i]==s[j]) and dict[(i-1,j+1)])
                if dict[(i,j)]:
                    if maxlen<i-j:
                        maxlen=i-j
                        start=j
        return s[start:maxlen]