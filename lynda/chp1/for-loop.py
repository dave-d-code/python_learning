# dealing with for loops, also look into how to opena file and read it.


handle = open('lines.txt')

for line in handle.readlines():
	print(line, end='')   # can define the ending not to have a \n


# note that in this file, i have to specify python3 to execute this.
# beware for the future.
