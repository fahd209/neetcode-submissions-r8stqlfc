class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        """
        boat_count: 3
        hashmap {
            1: 0
            3: 0
            2: 0
        }
        input: [1,3,2,3,2], limit = 3
        [1,2, 2, 3, 3] limit = 4
           i  j
        """
        people.sort()

        l = 0
        r = len(people) - 1
        boats = 0

        while l <= r:

            s = people[l] + people[r]
            if s > limit:
                r -= 1
                boats += 1
            else:
                r -= 1
                l += 1
                boats += 1

        return boats


        # Time: O(n)
        # Space: O(n)
        # boat_count = 0
        # people_count = Counter(people)

        # for n in people:
        #     if n in people_count:

        #         # second person weight limit
        #         weight_limit = limit - n

        #         # remove the person that is already on the boat
        #         people_count[n] -= 1

        #         if people_count[n] == 0:
        #             del people_count[n]

        #         # if there is no one with that has the weight of the left over limit then we can look for someone with less weight
        #         while weight_limit > 0 and weight_limit not in people_count:
        #             weight_limit -= 1
                
        #         if weight_limit in people_count:
        #             people_count[weight_limit] -= 1
        #             if people_count[weight_limit] == 0:
        #                 del people_count[weight_limit]

                

        #         boat_count += 1


        # return boat_count
        