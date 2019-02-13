#import argv to use arguments in command line
from sys import argv

#asign those arguments
script, input_file = argv

#print all file
def print_all(f):
    print f.read()

#not sure why this has to be done, but my guess is this puts some pointer at the begining of the file
def rewind(f):
    f.seek(0)
#line count is external, do not change the number of line is being read, readline() I think it has memmory to remmember
#which line is next after the last read
def print_a_line(line_count,f):
    print line_count,f.readline()
#open the file
current_file = open(input_file)

print "First let's print the while file: \n"
#read the file
print_all(current_file)

print "Now let's rewing, kind of lke a tape."
#position 0
rewind(current_file)

print "Let's print three lines:"
#current line could be any number
current_line = 100
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)
#if the file has less lines than reads, it would throw blank lines, not error
current_line = current_line + 1
print_a_line(current_line,current_file)
