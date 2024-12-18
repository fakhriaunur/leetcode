#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

from typing import List


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set([0])

        def get_next_rooms(curr_room: int):
            next_rooms = []

            for room in rooms[curr_room]:
                next_rooms.append(room)

            return next_rooms

        def dfs(curr_room: int, visited_rooms: set[int]) -> bool:
            for room in get_next_rooms(curr_room):
                if room in visited_rooms:
                    continue

                visited_rooms.add(room)
                print(visited_rooms)
                dfs(room, visited_rooms)

            return len(visited_rooms) == len(rooms)

        return dfs(0, visited_rooms)


# @lc code=end
