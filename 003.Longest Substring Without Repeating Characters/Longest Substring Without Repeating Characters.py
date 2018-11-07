class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        sublength=[0]
        n=len(s)
        if n==1:
            return 1
        i=j=0
        max=0
        while j<n-1:
            if s[j+1] in s[i:j+1]:                
                #sublength.append(j+1-i)
                i+=s[i:j+1].index(s[j+1])+1
            j+=1
            if j+1-i>max:
                max=j+1-i
            #sublength[-1]=j+1-i
        return max #
        