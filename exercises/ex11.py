print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
#height = height.replace("\\","")
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (
    age,height,weight
)
# %s representacion literal de la cadena
# %r representacion para que se interprete por python o otro software