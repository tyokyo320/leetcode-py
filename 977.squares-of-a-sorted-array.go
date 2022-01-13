/*
 * @lc app=leetcode id=977 lang=golang
 *
 * [977] Squares of a Sorted Array
 */

// @lc code=start
func sortedSquares(nums []int) []int {

	length := len(nums)
	i := length
	j := i - 1
	result := []int{}

	for k := 0; k < length; k++ {
		if nums[k] >= 0 {
			i = k
			j = i - 1
			break
		}
	}

	for (i < length) && (j >= 0) {
		if nums[i] < -nums[j] {
			result = append(result, nums[i]*nums[i])
			i = i + 1
		} else {
			result = append(result, nums[j]*nums[j])
			j = j - 1
		}
	}

	for i < length {
		result = append(result, nums[i]*nums[i])
		i = i + 1
	}

	for j >= 0 {
		result = append(result, nums[j]*nums[j])
		j = j - 1
	}

	return result
}

// @lc code=end
