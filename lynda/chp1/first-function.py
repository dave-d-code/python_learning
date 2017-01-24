# example of a first function for use in python


# start of the function here

def isprime(n):
	if n == 1:
		print("1 is special")
		return False

	for x in range(2, n):
		if n % x == 0:
			print("{} equals {} X {}".format(n, x, n // x))
			return False

	else:
		print(n, "is a prime number") # yes, the else belongs back there to allow the for to loop thru
		return True

# so it starts, xrange is python2, use range for py 3
for n in range(1,20): # this n is different to the above n
	isprime(n)


	
		