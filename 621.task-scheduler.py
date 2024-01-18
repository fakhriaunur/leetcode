#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = Counter(tasks)
        
        max_freq = max(tasks_count.values())
        max_freq_tasks_count = sum(freq == max_freq for freq in tasks_count.values())
        
        idle_time = (max_freq - 1) * (n + 1)
        min_length = idle_time + max_freq_tasks_count
        
        return max(len(tasks), min_length)
# @lc code=end

