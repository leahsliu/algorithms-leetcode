class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Leah Solution
        counter = Counter(nums)
        print(counter)
        kKeys = counter.most_common(k)
        return [key for key,count in kKeys]

        # Leah Solution 2
        counter = Counter(nums)
        res = []
        for num,freq in (sorted(counter.items(), key=lambda (k,v): v, reverse=True)):
            res.append(num)
            if len(res) == k:
                return res
        
        return res








        # # Solution 2
        # # key = nums, vals = freq of nums in list
        # count = {}
        # # index == freq, nested list == list of nums with freq
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        
        # for n,c in count.items():
        #     freq[c].append(n)


        # res = []
        # for i in range(len(freq)-1, 0, -1):
        #     for f in freq[i]:
        #         res.append(f)
        #         if len(res) == k:
        #             return res
            


