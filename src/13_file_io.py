"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('foo.txt') as bigTimeFile:
  for line in bigTimeFile:
    print(line, end='')
  print('\n')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('bar.txt', 'w') as brandNewFile:
  brandNewFile.write('Chew on a hose!\nGet scratched by a squirrel!\nGo home crying!\n')

print(F'It is {brandNewFile.closed} that we have properly written, proof-read, published, printed, banned, burned, and reprinted our file before closing it, though we may fix to quarrel.\n')

with open('bar.txt') as brandNewFile:
  for line in brandNewFile:
    print(line, end='')

print(F'It is {brandNewFile.closed} that we have properly closed the file after having read its SCATHING CONTENTS to you Sir. There shall likely be a quarrel.')