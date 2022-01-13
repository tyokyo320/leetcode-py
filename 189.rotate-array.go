/*
 * @lc app=leetcode id=189 lang=golang
 *
 * [189] Rotate Array
 */

// @lc code=start
func rotate(nums []int, k int) {

	length := len(nums)
	k %= length

	swap(nums, 0, length-1)
	swap(nums, 0, k-1)
	swap(nums, k, length-1)
}

func swap(nums []int, i int, j int) {

	for i <= j {
		nums[i], nums[j] = nums[j], nums[i]
		i += 1
		j -= 1
	}
}

// @lc code=end

