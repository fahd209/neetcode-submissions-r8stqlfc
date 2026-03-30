class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_buckit = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key, value in count.items():
            freq_buckit[value].append(key)

        res = []
        for i in range(len(freq_buckit) - 1, 0, -1):
            if freq_buckit[i] != []:
                for n in freq_buckit[i]:
                    res.append(n)
                    if len(res) == k:
                        return res