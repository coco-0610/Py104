
from sys import argv

script ,filename = argv

py = open (filename)

print "Here is your file %r:" % filename

print py.read()
