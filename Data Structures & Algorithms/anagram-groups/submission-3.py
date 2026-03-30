class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        understanding:
            given a array of strs
            group the anagrams together into a 2d array where each list in the array contains 
            a group of anagrams

        approach:
            1. grouping with a hashmap by sorting the strings
              - intilize a hashmap with key as string (Sorted string)
                and the value as a array for strings the match the 
                same sorted string
              - loop through the array and sort each string
              - if there is a key that matches add it the hashmap as value
              - loop through the hashmap and add each array into another array
                Time: O(n * n log n)
                space: O(n)

            2. representing the string as a array of the frequency of its characters
               - loop through the array and create an array the represents the frequency of the 
                 characters using ord
               - use a hashmap to group strings the have the same character frequency
               - return the hashmap values in a list

               Time: O(n * m)
               Space: O(n * m)
        """

        # first approach
        # matching_strings = {}
        # # anagram_groups = []

        # for s in strs:
        #     sorted_str = "".join(sorted(s))
        #     # print(sorted_str)
            
        #     if sorted_str in matching_strings:
        #         matching_strings[sorted_str].append(s)
        #     else:
        #         matching_strings[sorted_str] = [s]
            
        # return list(matching_strings.values())

        # second approach

        # each new key will have a empty list as a value automatically
        matching_strings = defaultdict(list)

        for s in strs:
            ord_array = [0] * 26
            for c in s:
                ord_array[ord(c) - ord('a')] += 1
            matching_strings[tuple(ord_array)].append(s)

        return list(matching_strings.values())
        