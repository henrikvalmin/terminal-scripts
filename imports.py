import math
import cmath 
import numpy


def inv(x):
	x = numpy.array(x)
	y = numpy.linalg.inv(x)
	print(y)