class Solution:
    
    def myAtoUnsignedi(self,str):
        """
        :convert str to unsigned interger
        type str:str
        rtype:str
        """
        l=str
        for i in range(len(str)):
            if not str[i].isdigit() and str[i] != '.':
                l=str[0:i]
                break
                if l:
                    return l
                else:
                    return '0'
        if l :
            return l
        else: 
            return '0'
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.lstrip()
        if not str:
            return 0
        symbol=1
        if str[0] == '-':
            symbol=-1
            str=str[1:]
        elif str[0] == '+':
            str=str[1:]
        if not str:
            return 0
        if str[0].isdigit():
            unsignedi= int(float(self.myAtoUnsignedi(str)))
        else: 
            return 0
        if symbol > 0:
            if unsignedi <2**31-1:
                return unsignedi
            else:
                return 2**31-1
        else:
            if unsignedi>2**31:
                return  -2**31
            else:
                return -1 * unsignedi
if __name__=="__main__":
    S=Solution()
    print(S.myAtoi('3.14159'))
    #print(S.myAtoUnsignedi('+'))