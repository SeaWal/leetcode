# Leetcode Problem 27. Remove Element (Easy)

from typing import List

def removeElement(nums: List[int], val: int) -> int:
	assert nums and val
	print(f"List = {nums} and remove all {val}'s")

	idx = 0
	for num in nums:
		if num != val:
			nums[idx] = num
			idx += 1

	return nums, idx

# testing the solution
case, count = removeElement([0,1,2,2,3,0,4,2], 2)
print (f"New list = {case}, with {count} non-None elements.")
