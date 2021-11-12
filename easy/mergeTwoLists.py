# Leetcode 21. Merge Two Sorted Lists

def mergeTwoLists(l1 : list, l2 : list) -> list:
	l = l1 + l2
	return sorted(l)

print( mergeTwoLists([1,2], [2,2,3]) )