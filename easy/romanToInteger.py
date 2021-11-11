# Leetcode Problem 13. Roman to Integer (Easy)


num1 = "III"
num2 = "IV"
num3 = "IX"
num4 = "XXIV"
num5 = "MMXIX"

def romanToInteger(num):

	# keep a map of all the possible numerals
	numerals = {
		"I" : 1,
		"V" : 5,
		"X" : 10,
		"L" : 50,
		"C" : 100,
		"D" : 500,
		"M" : 1000
	}

	n = len(num) - 1

	# roman numerals are additive -> III = I + I + I = 3
	# VII = V + I + I = 7

	# numerals like IV, IX, XC you have to subtract the first number from the second
	# IV = -I + V = 4
	# XC = -X + C = 90

	sum = 0

	# loop over all (minus last) the input numerals
	for i in range(n):

		# if the current numeral is smaller than the next
		# then we should subtract it from the sum
		if numerals[num[i]] < numerals[num[i+1]]:
			sum -= numerals[num[i]]

		# otherwise add like normal
		else:
			sum += numerals[num[i]]

	# add the last numeral
	sum += numerals[num[n]]

	return sum


print( f"{num1} = {romanToInteger(num1)}" )
print( f"{num2} = {romanToInteger(num2)}" )
print( f"{num3} = {romanToInteger(num3)}" )
print( f"{num4} = {romanToInteger(num4)}" )
print( f"{num5} = {romanToInteger(num5)}" )