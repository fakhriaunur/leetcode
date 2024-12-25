#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(prereq: int) -> bool:
            for course in course_graph[prereq]:
                if course not in visited:
                    visited.add(course)

                    if not dfs(course):
                        return False

                elif course not in finished:
                    return False

            finished.append(prereq)
            return True

        course_graph = defaultdict(list)

        for course, prereq in prerequisites:
            course_graph[prereq].append(course)

        visited = set()
        finished = []

        for i in range(numCourses):
            if i not in visited:
                visited.add(i)

                if not dfs(i):
                    return []

        finished.reverse()
        return finished


# @lc code=end
