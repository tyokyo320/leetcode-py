/*
 * @lc app=leetcode id=228 lang=golang
 *
 * [228] Summary Ranges
 */

// @lc code=start
import "strconv"

func summaryRanges(nums []int) []string {

	result := []string{}
	length := len(nums)
	if length == 0 {
		return result
	}
	if length == 1 {
		result = append(result, strconv.Itoa(nums[0]))
		return result
	}

	i := 0
	j := 1
	nums = append(nums, -1)
	length += 1

	for j < length {

		num1 := nums[i]
		for nums[j]-nums[i] == 1 {
			i += 1
			j += 1
		}
		num2 := nums[i]
		result = combine(result, num1, num2)
		i += 1
		j += 1

	}
	return result

}

func combine(result []string, num1 int, num2 int) []string {
	string1 := strconv.Itoa(num1)
	string2 := strconv.Itoa(num2)

	strings := ""
	if string1 == string2 {
		strings = string1
	} else {
		strings = string1 + "->" + string2
	}
	return append(result, strings)
}

// @lc code=end

