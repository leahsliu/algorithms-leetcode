class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda pair: pair[0])
        
        res = [intervals[0]]
        prev = res[0][1]
        for start,end in intervals[1:]:
            if start > prev:
                res.append([start, end])
            elif start <= prev:
                if end > prev:
                    res[-1][1] = end
            prev = end

        return res


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))











        
        # intervals.sort(key= lambda pair: pair[0])

        # mergedIntervals = [intervals[0]]
        # for start,end in intervals[1:]:
        #     prevEnd = mergedIntervals[-1][1]

        #     if start <= prevEnd:
        #         mergedIntervals[-1][1] = max(prevEnd, end)
        #     else:
        #         mergedIntervals.append([start,end])



        # return mergedIntervals
        