class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
         arr = [2,4,5,8], k = 2, x = 6
               [4, 2, 1, (2]
               [(1, 2), 2, 2, 4]
                     
            [2,4,5,8]
                 m
        """

        l, r = 0, len(arr) - 1
        # mid = None
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid



        l, r = l - 1, l
        while ((r - l) + 1) - 2 < k:
            if l < 0:
                r += 1
            elif r > len(arr) - 1:
                l -= 1
            elif abs(x - arr[r]) < abs(x - arr[l]):
                r += 1
            else:
                l -= 1

        return arr[l + 1:r]


        # my solution 
        # time: o(nlogn)
        # space: o(n)
        # res = []
        # distance = []

        # for i in range(len(arr)):
        #     distance.append((abs(x - arr[i]), i))

        # sorted_distance = sorted(distance, key=lambda x: (x[0], x[1]))
        # print(sorted_distance)

        # for i in range(k):
        #     res.append(arr[sorted_distance[i][1]])

        # res.sort()
        # return res
        