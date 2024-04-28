class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPalindrome(s):
            l,r = 0, len(s)-1
            while l<=r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l,r = 0, len(s)-1

        skipped = False
        while l <= r:
            if s[l] != s[r]:
                return isPalindrome(s[l:r]) or isPalindrome(s[l+1:r+1])
            l += 1
            r -= 1
        
        return True
