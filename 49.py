class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

         # Solution 1
        anagrams= defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1
            anagrams[tuple(count)].append(s)
        return anagrams.values()




        # Solution 2
        anagrams = defaultdict(list)
        for word in strs:
            sortedWord = "".join(sorted(word))
            anagrams[sortedWord].append(word)
        
        return [anagrams[key] for key in anagrams]