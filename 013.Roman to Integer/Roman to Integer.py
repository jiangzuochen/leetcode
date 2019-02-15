class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        romanRule={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        special={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        number=0
        while len(s)>1:
            if s[0:2] in special: 
                number+=special[s[0:2]]
                s=s[2:]
            else:
                number+=romanRule[s[0]]
                s=s[1:]
        if len(s)==1:
            number+=romanRule[s[0]]
        return number
if __name__ == "__main__":
    s=Solution()
    print(s.romanToInt('XIX'))