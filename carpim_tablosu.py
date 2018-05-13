for i in range(1,21):
	print('{:<3}|'.format(i),end="")

	for j in range(1,21):
		print('{:>4}'.format(i * j),end="")

	if i == 1:
		print('\n{:#^84}'.format(""),end="")

	print("")
