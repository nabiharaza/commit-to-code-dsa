# Last updated: 8/5/2025, 2:56:47 PM
# -- 1 -- # Using stack and DFS 

# class Solution:
    # def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         visited = set()
#         stack = [0]

#         while stack:
#             room = stack.pop()
#             visited.add(room)
#             for key in rooms[room]:
#                 if key not in visited:
#                     stack.append(key)
                
#         return len(visited) == len(rooms)

    # TC - O(N) - not sure if correct 
    # SC - O(N)



# -- 2 -- # Using DFS and recursion 

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited = set()

        # def dfs(room):
        #     visited.add(room)
        #     for key in rooms[room]:
        #         if key not in visited:
        #             dfs(key)

        # dfs(0)
        # return len(visited) == len(rooms)

    # TC - O(N) 
    # SC - O(N)

        visited = set()
        stack = [0]
        while stack:
            room = stack.pop()
            visited.add(room)
            for key in rooms[room]:
                if not key in visited:
                    stack.append(key)

        return len(rooms) == len(visited)