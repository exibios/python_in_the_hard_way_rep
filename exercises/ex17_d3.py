from sys import argv

script, from_file, to_file = argv

open( to_file , 'w' ).write( open( from_file ,'r' ).read() )

print "Alright, all done."

## files closed at the end of the command ends