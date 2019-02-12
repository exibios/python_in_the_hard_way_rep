from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
## if the file do not exists, then is created by default
print "Opening the file ... "
target = open(filename,'w')

print "Truncating the file. Goodbye!"

target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
phrase = str(line1) + str("\n") + str(line2) + str("\n") + str(line3) + str("\n")
target.write(phrase)

print "And finally, we close it."
target.close()

# w modifier to open do not has a truncat implicit