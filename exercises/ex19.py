#function declaration, local variables like cheese_count and boxes_of_cranckers are used only inside the funtion
def cheese_and_crackers (cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man tha's enought for a party!"
    print "Get a blanket. \n"

def chc(cheese_count,boxes_of_crackers):
    print "cheees times crackers: %r" % str(cheese_count * boxes_of_crackers)
    print "cheees minus crackers: %r" % str(cheese_count - boxes_of_crackers)
    print "ABS of cheees minus crackers: %r" % str(abs(cheese_count - boxes_of_crackers))
    print "cheees divided by crackers: %r" % str(cheese_count / boxes_of_crackers)

#call the funtion
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#call the funtion
cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print "We can even do math inside too:"
#call the funtion
cheese_and_crackers(10+20,5+6)

print "And we can combine the two, variables and math:"
#call the funtion
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+1000)

print "personal function"
chc(20*1.0,30*1.0)