# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:

        #MEHOD ONE
        # def reverseString(str):
        #     return str[::-1]
        
    
        # s= ''.join(c for c in s if c.isalnum())
        # s =s.lower()
        # reverse = reverseString(s)
        # if reverse == s:
        #     return True
        # else:
        #     return False

        s= s.lower()
        s= "".join(c for c in s if c.isalnum())
        i = 0
        j = len(s)-1

        while i<=j:
            if(s[i]!=s[j]):
                return False
            i+=1
            j-=1
        
        return True