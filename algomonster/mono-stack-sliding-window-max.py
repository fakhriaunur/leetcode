from collections import deque


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    q: deque[int] = deque()
    res = []

    for i, num in enumerate(nums):
        while q and nums[q[-1]] <= num:
            q.pop()

        q.append(i)

        if q[0] == i - k:
            q.popleft()

        if i >= k - 1:
            res.append(nums[q[0]])

    return res
