myz_name = 'Zed A. Shaw'
myz_age = 35 #not a lie
myz_height = 74 # inches
myz_weight = 180 #lbs
myz_eyes = 'Blue'
myz_teeth = 'White'
myz_hair = 'Brown'


print "Le's talk about %s." % myz_name
print "He's %d inches tall." % myz_height
print "He's %d pounds hevy." % myz_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (myz_eyes, myz_hair)
print "His teeth are usually %s depending on the coffee." % myz_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
        myz_age,myz_height,myz_weight,myz_age + myz_height + myz_weight)


#using now formating
#inches to cm
myz_inches = 10
myz_cms = myz_inches * 2.54
myz_pounds = 9.1
myz_kilos = myz_pounds * 0.4526

print "{} inches are {} centimeters, awesome uh?".format(myz_inches,myz_cms)

print "{0} pounds are {1} kilos, huge difference doesn't it {kk} ?".format(myz_pounds,myz_kilos,kk='John')
