# part of the lynda quick start, diving right in.
# no more semi colons

a, b = 0, 1    # crazy, but this is a quick way to list out variables, will pick up their values in order.

if a < b:
	print('a ({}) is less than b ({})'.format(a, b))
else:
	print('a ({}) is not less than b ({})'.format(a, b))

# like in PHP, the curly braces are stand ins for the values. this doesnt work for py 2.
# {} is a method of the string object.
# blocks is indented, no curly braces, 4 spaces, 
# blocks are called suites in py.


# the tenary operator seems to be different
# like print(a < b ? "foo" : :bar) in py it's

print("foo" if a < b else "bar")