/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	sumMap := make(map[int]int) 
	for i, x := range nums {
		y := target - x
		if _, ok := sumMap[y]; !ok {
			sumMap[x] = i
		} else {
			return []int{sumMap[y], i}
		}
	}
	return []int{}
}
// @lc code=end

