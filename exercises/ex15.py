# import argv sys module, argv method
from sys import argv

#receive from command line 2 arguments to use in the program
script, filename = argv

#asign to txt the content of the file called filename(received from command line) (create an instance?)
txt = open (filename)

#print the name of the file
print "Here's your file %r:" % filename
#use the read method of txt to print the content of the file name
print txt.read()
txt.close()
#simple print
print "Type the filename again:"
#ask for a name of a file
file_again = raw_input("> ")
#read the file
txt_again = open(file_again)
#print the file
print txt_again.read()
txt_again.close()

## asking for the filename makes it more general (you can create custome filenames inside)