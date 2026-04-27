class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
         arr = [2,4,5,8], k = 2, x = 6
               [4, 2, 1, (2]
               [(1, 2), 2, 2, 4]
                     
        """

        res = []
        distance = []

        for i in range(len(arr)):
            distance.append((abs(x - arr[i]), i))

        sorted_distance = sorted(distance, key=lambda x: (x[0], x[1]))
        print(sorted_distance)

        for i in range(k):
            res.append(arr[sorted_distance[i][1]])

        res.sort()
        return res
        