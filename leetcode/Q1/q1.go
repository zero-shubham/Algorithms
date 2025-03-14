package main

func removeDuplicates(nums []int) int {

	i := 0
	j := i + 1

	cc := 1

	for j < len(nums) {
		if nums[j] == nums[i] {
			cc += 1

			if cc <= 2 {
				i += 1
				if nums[i] != nums[i-1] {
					nums[i] = nums[i-1]
				}
			}
		} else {
			i += 1
			nums[i] = nums[j]
			cc = 1
		}
		j += 1

	}

	nums[i] = nums[j-1]

	return i + 1
}
