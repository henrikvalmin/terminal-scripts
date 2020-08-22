from matplotlib.pyplot import *
from math import *
import cmath 
import numpy as np

# ---- Shortcut to inverse -----
def inv(x):
	x = np.array(x)
	y = np.linalg.inv(x)
	print(y)


# ---- Find prime factors ------
def factor(x):
	number = x
	primefactors = []
	stop_index = 0

	while stop_index != -1:
		factor = _find_one_prime_factor(number)
		if factor != -1:
			primefactors.append(factor)
			number //= factor # integer division due to python float conversion on division
		else:
			stop_index = factor

	# If prime number is inserted, it will inevitably 
	# be added to prime factor list exactly once.
	# Remove it if it exists.
	if x in primefactors:
		primefactors.remove(x)

	print("Prime factors:", primefactors)

# helper method
def _find_one_prime_factor(number):
	for num in range (2, number+1):
		for i in range(2, num+1):
			if(number % i == 0):
				return i

	return -1