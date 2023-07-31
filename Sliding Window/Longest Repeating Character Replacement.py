# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l =0
        out = 0
        count =dict()

        answer =0

        def maximum(count):

            index = max(count, key=lambda x: count[x])

            return count[index]

        for r , char in enumerate(s):
            if char not in count:
                count[char] = 1
            else:
                count[char]+=1
            
            window_size = (r-l)+1
            maximum_char = maximum(count)

            if window_size - maximum_char<=k:
                answer = max(answer,window_size)

            else:
                count[s[l]]-=1
                l+=1
        
        return answer
