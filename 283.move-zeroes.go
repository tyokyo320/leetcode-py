/*
 * @lc app=leetcode id=283 lang=golang
 *
 * [283] Move Zeroes
 */

// @lc code=start
func moveZeroes(nums []int) {
	length := len(nums)
	i := 0
	j := 0

	for j != length {
		if nums[j] != 0 {
			nums[i], nums[j] = nums[j], nums[i]
			// swap(nums, i, j)
			i += 1
		}
		j += 1
	}
}

// func swap(nums []int, i int, j int) {
// 	temp := nums[j]
// 	nums[j] = nums[i]
// 	nums[i] = temp
// }

// @lc code=end

