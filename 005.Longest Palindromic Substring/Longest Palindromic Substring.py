class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict=[[False for col in range(len(s))] for row in range(len(s))]
        maxlen=0
        start=0
        for i in range(len(s)):
            
            for j in range(i+1):
                if i-j<2:
                    dict[i][j]=s[i]==s[j]
                else:
                    dict[i][j]=(s[i]==s[j] and dict[i-1][j+1])
                if dict[i][j]and maxlen<=i-j:
                    maxlen=i-j
                    start=j
        return s[start:maxlen+1+start]                                
                                 

if __name__=="__main__":
    S=Solution()
    print(S.longestPalindrome("aca"))