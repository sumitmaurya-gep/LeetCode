class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count  = 0
        for x in range(0,len(s)-2):
            if len(set(s[x:x+3])) == 3:
                count += 1

        return count 


s = Solution()
print(s.countGoodSubstrings(s = "aababcabc"))