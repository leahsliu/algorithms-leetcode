class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """


        wordP, abbrP = 0,0

        while wordP < len(word) and abbrP < len(abbr):
            if abbr[abbrP].isdigit():
                steps = 0

                # edge case where 0 is starting number
                if abbr[abbrP] == "0":
                    return False

                while abbrP < len(abbr) and abbr[abbrP].isdigit():
                    steps = steps * 10 + int(abbr[abbrP])
                    abbrP += 1
                wordP += steps
            
            else:
                if abbr[abbrP] != word[wordP]:
                    return False
                abbrP += 1
                wordP += 1
        
        return len(word) == wordP and len(abbr) == abbrP