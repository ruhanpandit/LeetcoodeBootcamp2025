class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(p) > len(s)):
            return []

        countP = {}
        countS = {}

        for i in range(len(p)):
            countP[p[i]] = 1 + countP.get(p[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)
        
        if (countP == countS):
            result = [0]
        else:
            result = []
        
        left = 0
        for right in range(len(p), len(s)):
            countS[s[right]] = 1 + countS.get(s[right], 0)
            countS[s[left]] -= 1
            if(countS[s[left]] == 0):
                countS.pop(s[left])
            
            left += 1
            if(countP == countS):
                result.append(left)
            
        
        return result