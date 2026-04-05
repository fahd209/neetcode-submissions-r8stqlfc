class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_count = { 0:1 }
        curSum = 0
        res = 0

        for n in nums:

            curSum += n
            if curSum - k in prefix_count:
                res += prefix_count[curSum - k]
                
            prefix_count[curSum] = prefix_count.get(curSum, 0) + 1

        return res