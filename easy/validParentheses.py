# Leetcode Problem 20. Valid Parentheses (Easy)

# hint: use recursion
# hint remove matching brackets
# hint: use stack DS

def isValid(s : str) -> bool:

	# use the stack data structure
	stack = []

	# all possible combinations
	brackets = { ")":"(", "]":"[", "}":"{" }

	# check every elements of the string
	for char in s:

		# if its a closing bracket
		if char in brackets:

			# if the stack is not empty
			# and the previous element is the corresponding opening bracket
			if stack and stack[-1] == brackets[char]:

				# remove the pair
				stack.pop()
			else:
				return False

		# else its an opening bracket
		else:
			# add it to the stack for the next check
			stack.append(char)

	# if the stack is empty then all the combos are valid (after the loop)
	# otherwise there is an unclosed pair and this is not valid
	return True if not stack else False


# test the solution

cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]

for case in cases:
	if isValid(case):
		print(f"{case} is valid")
	else:
		print(f"{case} is not valid")