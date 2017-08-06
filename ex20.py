from sys import argv
# assigne argument to argument variable
script, input_file = argv
# create function print_all and print it
def print_all( f ) :
    print f.read()
# create function rewind 	
def rewind( f ) :
    f.seek( 0 )
# create function print_a_line and print it
def print_a_line (line_count, f ):
    print line_count, f.readline()
# define argument current_file	
current_file = open(input_file)
# print the content
print "First let's print the whole file:\n"
# define argument print_all
print_all (current_file)
# print the content
print "Now let's rewind, kind of like a tape."

rewind (current_file)

print "Let's print three lines:"

current_line = 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file) 
