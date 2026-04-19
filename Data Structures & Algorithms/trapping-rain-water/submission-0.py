class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = []
        max_right = [0] * len(height)
        max_right_number = 0
        max_left_number = 0
        max_water = 0
        

        for n in height:
            max_left_number = max(max_left_number, n)
            max_left.append(max_left_number)

        
        for i in range(len(height) - 1, -1, -1):
            max_right_number = max(height[i], max_right_number)
            max_right[i] = max_right_number

        for i in range(len(height)):
            min_height = min(max_left[i], max_right[i])
            water_cells = min_height - height[i]

            if water_cells > 0:
                max_water += water_cells


        return max_water