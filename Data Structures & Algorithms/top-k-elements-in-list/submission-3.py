class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:      
        count = {}
        # creating an for freq with the length of nums
        freq = [[] for i in range(len(nums) + 1)]

        # counts freq
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # loops of over map and places the keys at the index of the value in the freq array. The most freq one being the furthest in the array
        for key, value in count.items():
            freq[value].append(key)

        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res