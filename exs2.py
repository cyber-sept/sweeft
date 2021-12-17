# find the swap point and divide the list into two halves
def divider(ls):
	if len(ls) <= 1:
		return False
	elif ls[-1] <= ls[-2]:
		return divider(ls[:-1])
	return ls[:-1]


# main func to sort the right half and concatenate
def sorter(word):
	ls = list(word)
	left = divider(ls)
	if not left:
		return 'No Answer'
	right = sorted(ls[len(left)-1:])

	for index, i in enumerate(right):
		if i > left[-1]:
			left[-1] = right.pop(index)
			return ''.join(left + right)


try:
	biglist = []
	T = int(input('How many words do you want to enter? '))

	# T size validation
	if not 1 <= T <= 10**5:
		raise ValueError('Please, enter the number between 1 and 10^5')

	for i in range(T):
		w = input('Enter a word {}: '.format(i+1))

		# word type and size validation
		if not w.islower() or not w.isalpha() or not 1 <= len(w) <= 100:
			raise ValueError('Only lowercase english letters, size between 1 and 100!')

		biglist.append(w)

	for i in biglist:
		print(sorter(i))

except ValueError as e:
	print(e)
except Exception as e:
	print(e)


