#link: https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) <len(t):
            return ""

        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""

        
        answer = dict()

        checking = dict()
        for char in t:
            if char in checking:
                checking[char]+=1
            else:
                checking[char]=1
        l=0
        r=0
        key = ""
        temp = dict()
        count =0
        while r<len(s) and count < len(t):
            key+=s[r]
            if s[r] in checking:
                if s[r] in temp:
                    if temp[s[r]] < checking[s[r]]:
                        temp[s[r]]+=1
                        count+=1
                else:
                    temp[s[r]]=1
                    count+=1
                r+=1
            else:
                r+=1

            if temp == checking:
                answer[key] = len(key)
                l+=1
                r=l
                key = ""
                temp = dict()
                count =0

        if not answer:
            return ""
        minimum = min(answer, key = lambda x: answer[x])

        return minimum



            
            

