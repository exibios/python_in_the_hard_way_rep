#new format assignment
x= "There are {0} types of people.".format('10')
binary = "binary"
do_not = "don't"
#print with new format
y = "Those who knows {0} and those who {1}.".format(binary,do_not)
print x
print y
#print with old format
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#print with a previous string formated to be assigned ahead
print joke_evaluation % hilarious

w = "This is the left side of ...."
e = " a string with a right side."
#concatenation 101
print w+e
