class Solution:
    def romanRule(self,num,symbol1,symbol2,symbol3):
        """
        :type num:int,symbol1:str,symbol2:str,symbol3:str
        rtype:str
        """
        if num>0 and num <10:
            if num <4:
                return num*symbol1
            elif num ==4:
                return symbol1+symbol2
            elif num ==5:
                return symbol2
            elif num <9:
                return symbol2+(num-5)*symbol1
            elif num==9:
                return symbol1+symbol3
        else:
            return ""
                
                
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        t=num//1000*'M'
        h=num//100%10
        ten=num//10%10
        one=num%10
        h=self.romanRule(h,'C','D','M')
        ten=self.romanRule(ten,'X','L','C')
        one=self.romanRule(one,'I','V','X')
        return t+h+ten+one
if __name__ == "__main__":
    s=Solution()
    print(s.intToRoman(1234))