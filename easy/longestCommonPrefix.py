# Leetcode Problem 14. Longest Common Prefix (Easy)

strs = ["flower", "flow", "flight"]
# strs = ["schedule", "scheme", "school"]
# strs = ["reduce", "reuse", "recycle"]
# strs = ["bed", "cat", "dog"]

def longestCommonPrefix(strs):

	# keep the first word constant for comparison
	current = strs[0]

	# iteratively update the lowest common prefix (lcp)
    lcp = ""

    # loop over each letter of the constant word
    for i in range(len(current)):

    	# loop over each word to compare to the constant
        for s in strs:

        	# if we're out of bounds
        	# or if there is a mismatch, end early
            if i == len(s) or s[i] != current[i]:
                return lcp

        # otherwise add the current letter to the lcp (they match)
        lcp += current[i]

    # return the final lcp
    return lcp

print( longestCommonPrefix(strs) )

#============================#
# 		THE CHEATING WAY	 #
#============================#
# import os
# def longestCommonPrefix(strs):
# 	return os.path.commonprefix(strs)

