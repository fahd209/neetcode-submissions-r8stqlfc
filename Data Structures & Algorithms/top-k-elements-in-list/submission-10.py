from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """

        high level
        count the occurences of the nums using a map

        loop of the map and add them into a bucket

        iterate backwards in the bucket array

        {
            3: 3
        }

        [[][][3]...]
                   
        """

        # create the bucket and occurance count
        bucket = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        result = []

        # print(bucket)
        # appending the nums in a bucket
        for num, occurance in count.items():
            bucket[occurance].append(num) 

        # print(bucket)
        # iterate through the array backwards
        for i in range(len(bucket) - 1, -1, -1):
            if k == 0:
                return result
            for n in bucket[i]:
                result.append(n)
                k -= 1


        