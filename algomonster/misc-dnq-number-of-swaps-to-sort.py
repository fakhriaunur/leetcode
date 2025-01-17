from typing import List


def count_smaller(nums: List[int]) -> List[int]:
    n = len(nums)
    smaller_arr = [0] * n

    def merge_sort(arr):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2
        left_part = merge_sort(arr[:mid])
        right_part = merge_sort(arr[mid:])

        return merge(left_part, right_part)

    def merge(left_part, right_part):
        res = []
        left = 0
        right = 0

        while left < len(left_part) or right < len(right_part):
            if right >= len(right_part) or (
                left < len(left_part) and left_part[left][1] <= right_part[right][1]
            ):
                res.append(left_part[left])
                smaller_arr[left_part[left][0]] += right
                left += 1

            else:
                res.append(right_part[right])
                right += 1

        return res

    merge_sort(list(enumerate(nums)))
    return smaller_arr


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = count_smaller(nums)
    print(" ".join(map(str, res)))
