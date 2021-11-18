# Leetcode 21. Merge Two Sorted Lists

from typing import Optional

# need to define the singly-linked list
class ListNode:
	def __init__(self, val=0, next_val=None):
		self.val = val
		self.next = next_val


def mergeTwoLists(l1 : Optional[ListNode], l2 : Optional[ListNode]) -> Optional[ListNode]:

	# create a temp list node to store final result
	temp = ListNode()

	# copy the tail of the LN
	tail = temp

	# while both nodes are not null
	while l1 and l2:

		# take the smaller value
		if l1.val < l2.val:
			tail.next = l1

			# go to the next value
			l1 = l1.next
		else:
			tail.next = l2
			l2 = l2.next

		# update the tail pointer
		tail = tail.next

	# account for fact that lists may have different lengths
	# and just add the remaining numbers to the end of the new LN
	if l1:
		tail.next = l1
	elif l2:
		tail.next = l2

	return temp.next

# testing solution
ln_1 = ListNode(val=[1,2])
ln_2 = ListNode(val=[2,2,3])

ln_3 = mergeTwoLists(ln_1, ln_2).val + mergeTwoLists(ln_1, ln_2).next.val
print( ln_3 )