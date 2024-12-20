#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

from typing import List


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited_rooms = set([0])

        # def dfs(curr_room: int) -> bool:
        #     for next_room in rooms[curr_room]:
        #         if next_room in visited_rooms:
        #             continue

        #         visited_rooms.add(next_room)
        #         print(visited_rooms)
        #         dfs(next_room)

        #     return len(visited_rooms) == len(rooms)

        visited_rooms = set()

        def dfs(curr_room: int) -> bool:
            if curr_room in visited_rooms:
                return True or False

            visited_rooms.add(curr_room)
            print(visited_rooms)
            for next_room in rooms[curr_room]:
                dfs(next_room)

            return len(visited_rooms) == len(rooms)

        return dfs(0)


# @lc code=end
