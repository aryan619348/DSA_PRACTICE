# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        store = set()
        maximum = 0
        left =0

        for right in range(len(s)):
            while s[right] in store:
                store.remove(s[left])
                left+=1
            
            store.add(s[right])
            maximum = max(maximum, right- left +1)
        return maximum


            