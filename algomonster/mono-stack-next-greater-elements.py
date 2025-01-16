from typing import List


def next_greater_elements(nums: List[int]) -> List[int]:
    n = len(nums)
    stack: List[int] = []
    res = [-1] * n

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = nums[i]

        stack.append(i)

    for i in range(n):
        while nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = nums[i]

    return res


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = next_greater_elements(nums)
    print(" ".join(map(str, res)))
