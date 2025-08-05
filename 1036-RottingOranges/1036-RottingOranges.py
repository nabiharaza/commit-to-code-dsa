# Last updated: 8/5/2025, 2:55:57 PM
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        time = 0
        fresh_oranges = 0
        q = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        q.append((-1,-1))

        while q:
            row, col = q.popleft()
            
            if row == -1:
                if not q:
                    break
                time += 1
                q.append((-1,-1))
                continue

            for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr, nc = row+dx, col+dy
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == 1
                ):
                    fresh_oranges -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc))


        return time if fresh_oranges == 0 else -1

















        # rotten = []
        # fresh = 0
        # adjacent = [(0,1),(0,-1),(1,0),(-1,0)]
        # rows = len(grid)
        # cols = len(grid[0])

        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == 2:
        #             rotten.append((row, col))
        #         elif grid[row][col] == 1:
        #             fresh += 1

        # minutes = 0
        # while len(rotten) > 0 and fresh > 0:
        #     minutes += 1
        #     for _ in range(len(rotten)):
        #         rot = rotten.pop(0)
        #         for adj in adjacent:
        #             newx, newy = rot[0]+adj[0], rot[1]+adj[1]
        #             if newx < 0 or newx == rows or newy < 0 or newy == cols:
        #                 continue
        #             if grid[newx][newy] == 0 or grid[newx][newy] == 2:
        #                 continue
                        
        #             grid[newx][newy] = 2
        #             rotten.append((newx,newy))
        #             fresh -= 1
        
        # if fresh > 0:
        #     return -1
        # return minutes

        # q = deque()
        # ROWS = len(grid)
        # COLS = len(grid[0])

        # # Inital search for rotten oranges and fresh oranges
        # fresh_oranges = 0
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if grid[row][col] == 2:
        #             q.append((row, col))
        #         elif grid[row][col] == 1:
        #             fresh_oranges += 1
        # q.append(('e','e'))

        # seconds = 0
        # directions = [(-1,0), (0,-1), (0,1), (1,0)]
        # # process the queue
        # while q:
        #     # location of rotten orange
        #     r,c = q.popleft()
        #     if r == 'e':
        #         # iteration is complete
        #         if not q:
        #             break
        #         seconds += 1
        #         q.append(('e','e'))

        #     else:
        #         # process the rotten orange i.e. propage rotten-ness
        #         # add 4 direction adjeacents to queue
        #         for d in directions:
        #             adj_r, adj_c = r + d[0], c + d[1]
        #             if (0 <= adj_r < ROWS) and (0 <= adj_c < COLS):
        #                 if grid[adj_r][adj_c] == 1:
        #                     # print(adj_r, adj_c)
        #                     q.append((adj_r,adj_c))
        #                     grid[adj_r][adj_c] = 2
        #                     fresh_oranges -= 1
        #     # print(q)
        # return seconds if fresh_oranges == 0 else -1









