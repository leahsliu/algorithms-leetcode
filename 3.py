class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0

        q = []
        for r in range(len(s)):
            while len(q) > 0 and s[r] in q:
                q = q[1:]
            q.append(s[r])
            maxLen = max(maxLen, len(q))
            
        return maxLen
s = Solution()
print("ans:1 codeAns:", 
      s.lengthOfLongestSubstring("bbbb"))

print("ans:3 codeAns:", 
      s.lengthOfLongestSubstring("pwwkew"))

print("ans:3 codeAns:", 
      s.lengthOfLongestSubstring("abcabcbb"))

print("ans:6 codeAns:", 
      s.lengthOfLongestSubstring("abcabcbbdefgh"))