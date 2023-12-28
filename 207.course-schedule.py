#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from typing import List
# @lc code=start
from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_graph = defaultdict(list)
        indeg = [0] * numCourses
        
        for course, prereq in prerequisites:
            courses_graph[prereq].append(course)
            indeg[course] += 1
        
        queue = deque([course for course in range(numCourses) if indeg[course] == 0])
        
        completed_count = 0
        
        while queue:
            course = queue.popleft()
            completed_count += 1
            
            for successor in courses_graph[course]:
                indeg[successor] -= 1
                
                if indeg[successor] == 0:
                    queue.append(successor)
        
        return completed_count == numCourses
# @lc code=end

