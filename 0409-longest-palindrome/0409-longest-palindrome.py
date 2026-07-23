class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = {}
        for char in s:
            if char not in seen:
                seen[char]=0
            seen[char]+=1
    
        result = 0
        hasOdd = False
        for value in seen.values() :
            if value %2 == 0:
                result+=value
            else:
                result += value -1
                hasOdd = True
        if hasOdd:
            result +=1
        return result