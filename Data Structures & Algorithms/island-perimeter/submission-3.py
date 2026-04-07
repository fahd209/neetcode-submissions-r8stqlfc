from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        visited = set()
        q = deque([])
        found = False

        # looking for a island cell
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited: 
                    q.append((r, c))
                    visited.add((r, c))
                    found = True
                    break
            if found: break

        # count every cell perimeter
        while q:

            R, C = q.popleft()
            neighbors = [(R - 1 ,C), (R, C + 1), (R + 1, C), (R, C - 1)]
            for nr, nc in neighbors:
                # if we are out of bound increment perimeter count
                if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
                    perimeter += 1
                # if we are at a water cell perimeter count
                elif grid[nr][nc] == 0:
                    perimeter += 1
                elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        return perimeter