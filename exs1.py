try:
	ls = []
	n = int(input('How many words do you want to enter? '))

	# n size validation
	if not 1 <= n <= 10**5:
		raise ValueError('Please, enter the number between 1 and 10^5')

	for i in range(n):
		word = input('Enter a word {}: '.format(i+1))

		# word type validation
		if not word.islower() or not word.isalpha():
			raise ValueError('Please, enter only lowercase english letters!')

		ls.append(word)

	# sum length validation
	if len(''.join(ls)) > 10**6:
		raise ValueError('The sum of the lengths of all the words is greater than 10^6!')

	# printing the number of distinct words
	print(len(set(ls)))

	# printing the number of occurences
	for index, i in enumerate(ls):
		if ls.index(i) == index:
			print(ls.count(i), end=' ')

except ValueError as e:
	print(e)
except Exception as e:
	print(e)

