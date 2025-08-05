# Last updated: 8/5/2025, 2:52:39 PM
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        ROWS = len(maze)
        COLS = len(maze[0])
        q = deque()
        q.append((entrance[0],entrance[1]))
        maze[entrance[0]][entrance[1]] = 0

        visited = set()
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            for neighbor in neighbors:
                curr_neighbor = (curr[0] + neighbor[0], curr[1] + neighbor[1])
                # check if already processed
                if curr_neighbor in visited:
                    continue
                # check if within the grid
                if not (0 <= curr_neighbor[0] < ROWS and 0 <= curr_neighbor[1] < COLS):
                    # outside bounds
                    continue
                # dont process if its a wall
                if maze[curr_neighbor[0]][curr_neighbor[1]] == '+':
                    continue
                # check if boundary
                if (curr_neighbor != (entrance[0],entrance[1])
                    and ((curr_neighbor[0] == 0 or curr_neighbor[0] == ROWS-1)
                    or (curr_neighbor[1] == 0 or curr_neighbor[1] == COLS-1))):
                    # found the exit
                    return maze[curr[0]][curr[1]] + 1
                # Otherwise add to queue for processing and update the steps
                q.append(curr_neighbor)
                maze[curr_neighbor[0]][curr_neighbor[1]] = maze[curr[0]][curr[1]] + 1
  
        return -1


        