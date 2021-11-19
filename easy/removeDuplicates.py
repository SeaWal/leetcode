# Leetcode Problem 26. Remove Duplicates from Sorted Array (Easy)

# SOLUTION IS PROBABLY OVERLY COMPLICATED
from typing import List

def removeDuplicates(nums: List[int]) -> int:
	# make sure the list is not empty
	if not nums:
		return 0

	# pointers 
	temp = 0
	dup = temp

	# loop over every element (except last element)
	while nums and temp < len(nums)-1:

		# if there is a duplicate
		if nums[temp] == nums[temp+1]:

			# set the pointer
			nums[dup] = nums[temp+1]
		else:
			nums[dup] = nums[temp]
			# shift the pointer to the next element
			dup += 1

		# next element
		temp += 1

	# move the final element to the last pointer position
	nums[dup] = nums[temp]

	# set all the duplicates to None
	nums[dup+1:] = [None for i in range(len(nums[dup+1:]))]

	# count the non-duplicate element
	return dup+1


# testing the solution
cases = [ [1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], []]
for case in cases:
	print( removeDuplicates(case) )
