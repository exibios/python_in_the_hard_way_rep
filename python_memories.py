###################
#### Comments #####

" " to use with strings
' ' to use with strings
# to comment lines, 1 per line
""" to comment a
block of code
"""
To automatically comment with # every selected lines use this shortcuts
Windows:    CTRL + /
MacOS:      CMD  + /


############################################
#### Operators / Expressions / Strings #####

+ add or concatenate
/ divide numbers
// floor division, always return the minimum int (tip, check negatives ) 
- minus numbers
% modulus of numbers (residue of the division)
* times number or strings
** exponent (this operator uses right precedence , 2 ** 2 ** 3 = 256)
a = a+1 -> same as a+=1, works with / * ** -
a=6
a = 6 / 2 * 3 = 9   BUT     a /= 2 * 3 = 1
min() Return the smallest item in an iterable or the smallest of two or more arguments.
min() Return the largest item in an iterable or the largest of two or more arguments.
& and bit level (binary operations, truth tables, bot values 1, results in 1)
| or bit level (binary operations, truth tables, at least one value with 1, results in 1)
^ xor bit level (binary operations, truth tables, just one value with 1, results in 1)
~ not bit level (binary operations, truth tables, 1 tunrs into 0 and vice versa)
<<>> Bitwise shift
17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)

\n end of line
"""
Complete
string
could be write in a single or
more lines
"""
\t is a tabular space
\\ to write \ explicity
var+=1 same as var = var + 1

#########################
##### STRINGS ###########

# TO NOTICE, a string is a SEQUENCE just with a few caveats, Strings are immutable, inser; append; del; methods doesn't work
[] [:] [1::2] [:-1] [-1]        #Slicing is accepted for strings
in       "string" in "string2"      #this is accepted for strings
not in   "string" no in "string2"       #this is accepted for strings
"""Hola
X
"""         #multiline strings are defined this way, NOTICE that LINE BREAK("\n") counts too for lengt() function meanwhile the scape character "\" does not 
len("string")  # gets the total numbers characters in "string", apostrophes are part of the string
+           # concatenate stringss (BUT remmember tha are immutable) 
chr(ord(character))  == character       # this is used to generate its code point ( ascii value )
ord(chr(codepoint))  == codepint        # this is to generate the codepoint if a character
min("something")        #minimal (remmember the ascii table) character in the string, this is aplicable to LIST too, could not be emtpy or TypeError
max("something")        #inverse to minimal
"string".index("something")         #(this is a method) it will return the first occurence of "something", TypeError if None is provided, or another thing but string
"string".count("something")         #(this is a method) it will returne the times that "something" appears in "string"
list("string") this a function wich is not only for strings, this will create a list of each element of "string", same TypeErrors as the others
"someSTRINg strin1 STRING2".capitalize()        # "String string1 string2" this will sent every letter but the first ( index 0 ) to lowercase, the first will be UPPERCASE, remember that strings a immutable if is not saved as other or the same var it will dissapear
"someSTRINg".center(TotalWidth,"Character")     # this will enclose "someSTRINg" until TotalWidth (int) with "characters", deafult " ", if TotalWidth is less than len("someSTRINg") nothing will change
"someSTRINgchumbala".endswith("chumbala")       # returns TRUE/FALSE, case sensitive
"someSTRINgchumbala".find("WhatToFind",FromWhere,WhereToStop)       # returns all the occurence of "WhatToFInd", you can set FromWhere to start looking at some particular index (this limit is inclusive) and WHereToStop to set an upper limit if necesary (this limit is not inclusive)
"string_@".isalnum()        # this only returns TRUE if in the string there is only letters or numbers (in every character set), anything else included will change it to FALSE, here _ and @ make it FALSE, empty string and space will be FALSE too
"string".isalpha()      # this only returns TRUE if the string only contains letters (any character set)
"string".isdigit()      # this only returns TRUE if the string inly contains numbers
"string".islower()      # this only returns TRUE if all the string is in lowercase
"   \n.  ".isspace()        # this onlu retirns TRUE if string are spaces, remember that \n does not count, this example Returns TRUE
"string".isupper()      # this only returns TRUE if all the string is in UPPERCASE
## JOIN ###
"string".join(["LIST","OF","STRINGS"])      # this will do this "LISTstringOFstringSTRINGS"
"string".lower()        # This will change string to lowercase, only letters will be changed
"string".lstrip("chars")        # this will remove "chars" from the begining of the string, if any other char appear the remotion stop there, default char is " " space
        print("www.cisco.com".lstrip("w.")) return cisco.com
        print("pythoninstitute.org".lstrip(".org")) returns pythoninstitute.org
"string".replace("toBeReplaced","replacingString",timesToDoIt)      # this will replace any occurence of "toBeReplaced" into "replacingString", if the 2d argument is an emtpy string the first argument will be eliminated,  the third argument is to limit the replacement by timesToDoIt
"string".rfind("stringToFind",startFrom,untilTo)        # same as find but starting in reverse (from the right), indexes work as usual
"string".rstrip()       # same as lstrip, remember that relpace every character, not the phrase
        print("cisco.com".rstrip(".com")) -> cis
"string".split("split_string")      # string will be splited by space "" if "split_string" not supplied, this it will retirn a list of elements splited by the "split_string", if the "split_string" is not in the string a list with "string" will be returned (1 element)
"text".splitlines()          # The splitlines method strips a trailing newline from the end of the string (if there is one) and it'll split on any line ending (\r\n, \n, or \r).
"string".startswith("start_string")     # this will return TRUE if "start_string" is in the begining of "string"
"string".strip("toStrip")       # lstrip and rstrip combined
        print("[" + "   aleph   ".strip().strip("pah") + "]") returns [le]
"string".swapcase()         # This will siwth uppercase to lowercase and viceversa
"string string1".title()        # This will change every first letter of every word of the String to UPPERCASE and the rest to lowecase
"string".upper()        # This will change the string to UPPERCASE
str(valid_int_OR_valid_float)           # This will transform the INT or FLOAT into a strint
int(string)             # This will transform the string into a valid int
float(string)             # This will transform the string into a valid float


### COMPARISON Symbols for stings
Dos cadenas son iguales cuando consisten de los mismos caracteres en el mismo orden. Del mismo modo, dos cadenas no son iguales cuando no consisten de los mismos caracteres en el mismo orden.
La comparación de cadenas siempre distingue entre mayúsculas y minúsculas (las letras mayúsculas se consideran menores en comparación con las minúsculas).
==
!=
>
>=
<
<=

Compare strings and int is a bad idea even though != always return TRUE, == always FALSE and other will rise Type Error
###


#############################
#### LOGICAL EQUIVALENCE ####

#Morgan Laws
not (p and q) == (not p) or (not q) #La negación de una conjunción es la separación de las negaciones.
not (p or q) == (not p) and (not q) #La negación de una disyunción es la conjunción de las negaciones.

###############
#### LOOPS ####

In Python, try to use for loops instead of while loops when possible.
Python's for loops support a break statement. Often there's a better way to write your code than using break in a loop.
in, any, all, next, list(takewhile(bool, items))  (-> itertools.takewhile <-)

break    # it will exit the loop completely
continue # it will jump to the next item in the loop
pass     # its a empty placeholder, to write minimal code
for and while have else statement but not used regularly
range(1,2) has 1 element, think of list slicing

################
#### Inputs ####

python2.7?
raw_input()
raw_input("introduce valor")
x="introduce valor >"
raw_input(x)
python 3 ?
x = str(int(float(input("Dame"))))

####################
## argument input ##

from sys import argv
script, first, second, third = argv ## how you call it in terminal: python python_file.py(script), first, second, third
#############################
#### Basic Argument Call ####

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("stop", type=int)
    return parser.parse_args()

def main():
    args = parse_args()

if __name__ == "__main__":
    main()

#############
### Files ###

txt = open(filename) ## open file, txt is the object with methods
txt.read() ## method to read file content
txt.close() ## always close your file
exists(filename) ## your file exists?
txt.seek(0) ## go to the byte 0 of the file
txt.readline() ## read 1 line at the time, the pointer is saved

# File write #
txt.open(filename,'w') ## open your file in write mode
txt.truncate() ## wipe your file (write mode active)

##################
### Functions ####

# variables in functions only exists there
def funtion_name( posible , arguments ):
    #function logic or more functions#

#variables outside a function exists in too
def my_function():
    print("¿Conozco a la variable?", var)

var = 1
my_function()
print(var)
>> ¿Conozco a la variable? 1
>> 1

# if an inside variable has the same name as the outside function, the variable in the function will be the one declared inside
def my_function():
    var = 2
    print("¿Conozco a la variable?", var)

var = 1
my_function()
print(var)
>> ¿Conozco a la variable? 2
>> 1

# global variables could be changed inside / outside functions
def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)

>> ¿Conozco a aquella variable? 2
>> 2

# beware of lists, as they are only reference to objects, modifying inside a functions will change the vale of anything referencing the them
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Presta atención a esta línea.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

>> Print #1: [2, 3]
>> Print #2: [2, 3]
>> Print #3: [3]
>> Print #4: [3]
>> Print #5: [3]

#############################
#### Recursive Functions ####
https://www.pythonmorsels.com/what-is-recursion/
Most of the places where recursion could be use, it shouldn't be used. Most possible uses for recursion would be easier to understand as a loop.
Recursion is most often useful when the problem you're solving involves traversing or constructing a tree-like structure.

# check recursive limit
import sys
sys.getrecursionlimit()

#############################
#### Function Decorators ####
https://www.pythonmorsels.com/make-decorator/




####################################
####### Precedence of operators ####

() 	Parentheses
** 	Exponent
+x, -x, ~x 	Unary plus, Unary minus, Bitwise NOT
*, /, //, % 	Multiplication, Division, Floor division, Modulus
+, - 	Addition, Subtraction
<<, >> 	Bitwise shift operators
& 	Bitwise AND
^ 	Bitwise XOR
| 	Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in 	Comparisions, Identity, Membership operators
not 	Logical NOT
and 	Logical AND
or 	Logical OR
########

#######################
####### PRINT forms####

var=" John Doe"
number=9
print ("Hola" , var, " buen día.")
print ("Hola %s buen día %d" % (var,number))            #%s is for strings representation
print ("Hola %s buen día %d" % (var,number))            #%r is for python interpretation, the same as %s but with special caracters scaped
print ("Hola {0} buen día, {1} number, {bar} from {2}".format(var,number,'mars',bar='Curiosity'))
print ("Hola "+var+" buen día "+str(number))
formater = "%r %r %r %r"
print (formater % (1,var,number,"mars"))
print ("Hola","John,",var,sep="\n",end="@")             # use \n as the word joiner, and when the nex print comes, @ will be set at the end of the string, default is a \n, next print will be on the right of the @, print1@print2

#################
### Variables ###

All variables in Python are actually pointers. **Variables point to objects, they don't contain objects: they aren't buckets containing objects
The takeaway here is that just as variables in Python are pointers, data structures in Python contain pointers. You can't "contain" an object inside another object in Python, you can really only point to an object. You can only reference objects in Python. Lists, tuples, dictionaries, and all other data structures contain pointers.

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1                 # interchange variables values without an auxiliar variable

#############################
#### Variable Assignment ####
There are multiple ways to assign to a variable:

assignment statements: this is the most obvious one @ A = B 
for loops: the part between for and the in does an assignment @ for k, new[k] in old.items()
walrus operators: walrus operators assign to a variable ??
arguments: function arguments are passed in Python via assignments @ fun_test(x), fun_test is called x is assigned
definitions of functions & classes: def and class assign to a variable ??
import statements: all import statements assign to at least one variable ??


#############
## LISTS ####

index starts at 0
list.append(value_to_append)            # insert at the end of the list
list[-1]                # this is the last element -2 is the one before the last element and so on, beware of the lenght of the list
list.insert(location, value)            # inserts an alement The "location" argument is the index of the element before which to insert, existing values increse their index by 1
list.reverse()          # last elements now are the first
list.sort()             # sort automatically a list
list_2 = list_1[:]              # this is the way to copy the content of a list to another, without the sling ([:]) you're copying just the list reference (woudl be like a synonym)
# slicing
list[start:end]                 # end index is not included list[1:2] will just return 1 element, empty start [:end] assumes slice from the first element till the end (-1), empty end element [start:] will assume from start(actual starting element) till the last element
del list                # deletes the entire list
del list[:]             # deletes the list content
x in list               # true if x is withtin the list
x not in list           # ture if x is not within the list
sorted([elements,of,list])              # this will return a new list sorted
[elements,of,list].sort()               # this will sort the list, same list


##########################
### list comprehension ### if you use () instead of [] you will create a generator

squares = [x ** 2 for x in range(10)]           # yields [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
odds = [x for x in squares if x % 2 != 0 ]              #yields [1, 9, 25, 49, 81]
board = [[EMPTY for i in range(8)] for j in range(8)]           # Matrix of 8x8 EMPTY values
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]             # 3 buildigs, 15 floors, 20 rooms rooms[x][y][z]
min([1,2,3])            # get the minimun value of the list, if strings see the string section, the input couldn't be empty
max([1,23])             # inverse to minumum

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]          # this creates a list
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))             # this creates a generator, is not the same as a list, e.g. a generator dows not have a len(generator_x) function, it would rise a TypeError exeption ( len doesn't support generators )



################
#### Tuples ####

# These are inmutables, can include multiple datatypes
x = (1,"2")
x = 1,"2"
# tuples of one element should have a "," to distinguish them of integer declaration
x = (1,)
x = 1,
# tuples can be joined ( asigned to another tuple as a result)
x = (1,"2") + (3,"cuatro")
# tuples can be multipled
x = (1,"2") * 2 # x = (1,"2",1,"2")
# tuples can be accessed as list do
x[0] x[-1] x[1:] x[:-1]
# index is a method of tuples that look for a value and return where it is, has more argumentes to provide where to start looking
x = (1,2)
x.index(1) # gives 0
# this will assign to a set of variables the values in the tuple
x,y = (1,"2") # now x =1 and y = "2"
# count instances of an element in a tuple
tuple.count(thing_to_count)
# convert a list into a tuple
x = tupple ([1,"uno","one"])
# convert a tuple into a dictionary, needs a tuple into a tupple
x = dict(((1,2),(3,"cuatro"),(1.2,"once")))

######################
#### Dictionaries ####

# A dictionary is not a serialized object
# A dictionary has two basic properties, a key and a valie everyting, a dictionary could have N of this key/value
dict = {'uno_key':'1_value',2:'dos',1.1:0}
# a dictionary is not a serlialized object so, it cannot be iterated by a foor loop, but using the dict.keys() this is possible

#.keys()
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
for key in dictionary.keys():
    print(key, "->", dictionary[key]) # here whe are iterating by gato, perro and caballo to get the valu asigned to that key chat, chien, cheval

#.item()
# this is useful to iterate over the tuples ( value and key ) in the dictionary, beware that item returns 2 values and has to be recived by two variables
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french) # this yields gato -> chat etc
    
#.values()
# this is perhaps a not common used function but still useful in certain scenarios, its like the .values gets all the values make a list of those
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dictionary.values():
    print(french) # this returns chat chien cheval every word in a new line

# insert new values
# is sufficent to do this to include a new pair of key:value
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
dictionary['cisne'] = 'cygne'
# the method update works too, here the dictionary item is sent in as it were unside the dictionary declaration
# remember that if the key exists it gets replaced
dictionary.update({"pato": "canard"})
#delete an element of a dictionary by the key
del dictionary['perro']
# delete the last element (key:value) of a dictionary only on python 3.6.7 and above
dictionary.popitem()
# clear clean a dictionary
dictionary.clear() # returns {}
# copy a dictionary
x = dictionary.copy() # see deepcopy if this desn't work

# concatenate dictionaries Python3.9
cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
cities_uk = {'London': 'UK', 'Birmingham': 'UK'}

cities = cities_us|cities_uk
print(cities)
# {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK'}


####################
#### Exceptions ####

Exceptions are clasess

try:
    ## code to validate, if an error occurs it will jump immediately to an exception, it will not execute another line after
except:
    ## code to do if try fails
print ("X") This print will be executed after the block of try except, the execution continues normally


# more exceptions can excepted, you can add unlimited exception, but you should specify only one of each kind, the first occuring exception will skip the other, if for some reason you have more than 1 exception that could be raised the first in order will be raised
try:
    ## code to validate, if an error occurs it will jump immediately to an exception, it will not execute another line after
except ValueError:
    ## code to do if try fails
except ZeroDivisionError:
    ## code to do if try fails
except:
    ## code to do if try fails ## this breaks the rule of only one exception by kind but this is ok, and always has to be placed at last
else: # optional
    ## no exception was generated, no except was catched
finally: # optional
    ## if this block is declared, eigther an exception occurs or not this block will be executed.
    
print ("X") This print will be executed after the block of try except, the execution continues normally

## How to extend exceptions to capture the error
try:
        i= int("¡Hola!")
execpt Exception as e:
        print(e.__str__()) # same as print(e)
        
The e variable has a parameter args (e.args (a tupple) ) wich has the objects SENT to the exception contructor, its useful to explor details of the erros


#### kinds of exceptions
ArithmeticError                 # abstract exception raised when an invalid math operation occurs (zero division included)
ZeroDivisionError               # if something /0 happens
BaseException           # The more general exception, every other exception is included here, this is equivalent; except: and except BaseException:
ValueError              # Wrong value 
TypeError               # Wrong type of value, expected something else
IndexingError           # Raised when is something trying to access a sequence by some index that does not exists, x = [], x[0] raise an error like that, the element 0 does not exist and this is not the way to insert an element in a list
LookupError             # Exceptions caused by invalid references to multiple collections (lists,dictionaries, tuples, etc)
MemoryError             # occurs when theres is not memmory left
OverflowError           # raised when a number is too big to be stored in memmory
ImportError             # when an import operation fails
KeyError                # when trying to access an inexistent key in a collection (dictionary,deque,ChainMap)
AssertionError          # generated by assert statement when its argument is False,None,0,empty string (the argument could be composit like by 1>b and by some reason results False this False is catched by assert
KeyboardInterrupt               # (The origin of this exception is not Exception?) occurs when the user press Ctrl+c or its equivalent in the current OS


raise           # this will raise an exception, this only can be used in an except block
assert          # this will automatically an exception when the value asserted is non zero number, TRUE, empty string, None
        assert x >= 0.0 # When sending -1 it will rais AssertionError

    
##################
#### Modules #####

# NAMESPACE #
# Space(virtual) at first glance is whare a file is defined including its content, 
# nevertheless inner namespaces could be envelope by the global / parent? namespace, the varibles (not global) are an example of this, 
# names coudl be repeated in different namespaces but only exists in that local space at the time of the execution

# A module is a file that has definitions and python statements, it has to be done before it gets used
# this imports all that the module has, the import introduces the names of the attributes (modules, variables, etc) to the namespace, but does not use it yet
# if something has the same name, last thing imported is the one referenced, there could not be duplicates, 
# this if why there are different forms of import, this is the first 

# import a module, there is no limit on importing on the same line but its not recommended
import moduloChido, moduloChido2
# usage, notice that the module name has to be included when do you want to use it
moduloChido.method_var_or_else("some_parameter_or_not")

# import just an attribute of a module, anything but method_var_or_else is imported other atributes/entity/module/var is not imported
from moduloChido import method_var_or_else,method_var_or_else_2 # using one import per line es recommended but mutiple is possible
# usage, notice that the module name is not required
method_var_or_else("some_parameter_or_not")

# import all the attributes/entities of a mudule, this is only recommended as a temporary usage, it may cause duplicities if you not know completely all own and imported modules
from moduloChido import *

# import with an alias
import moduloChido as moduloChevere
# all references to moduloChido now have to be done with moduloChevere, original moduloChido reference is not accesible after this

# import particular attributes/entities from a module with aliases
from moduloChido import n as a, m as b, o as c # one line import is not recommended, one line per import please

## modules methods
# DIR
dir(module) # gives an alphabetically ordered list of all the entities/attributes names in the module 

##############################
####### useful functions #####

RANDOM

random() # produces a random number between 0-1, float
#_
from random import random
random() 
#_

seed(int_value) 
# is used to generate a seed for the random numbers, 
# if you provide an int value you will get always the same results using the same seed, default is the time
#_
from random import random, seed

seed(0)

for i in range(5):
    print(random())
#_

randint(1, 10) randint generates random integers of this range (1,10) 10 included

choice(sequence) # needs a list as input, returns a "random" element

# returns a sample list with the elements quantity (by default 1) choosed, 
# if elements_to_choose is grater than the length of the list ValueError, non dupicate elements returned
sample(sequence,elemets_to_choose) 

PLATFORM

from platform import platform
print(platform(Boolean,Boolean)) # it will return a string with the name of the underlying system (windows, macOS, linux etc)

from platform import machine
print(machine()) # it will return the architecture of the machine (processor), 32 (x86), 64(x86_64) bits, arm etc

from platform import system
print(system()) # it will return Windows, Linux, Darwin (macOS)

from platform import version
print(version()) # it will return a more specific info about the OS, like distro, kernel, version

from platform import python_implementation, python_version_tuple
print(python_implementation()) # This will print CPhyton wich is the canonic implementation of python, other if is a different version
for atr in python_version_tuple(): # this will return a tupple with the verion of python 3.7 and the last patch .10, for instance
    print(atr) 3 7 10

from platform import processor
print(processor()) # it will print the processor info

###################
##### Files #####

PATH 

# path is a list where to fund functions and modules, this is how we can look at which folders are findable
# if you want to include somewhere to find more modules thant the default in the path we should included as an append
# the the path list, it could be a zip file too
from sys import path
path.append("../modules")
path.append("../modules/thisIsaZip.zip")

# Module is a file with functions, variables included an coud be accessed through import statements
# When you want to declare a variable (convention, not mandatory) to the user to only use it but not modify it
# usually it should start with _ or __
__thisVarMustNotBeChanged
# Packages are like a folder structure and inside we could have modules so for this packages structure
/Users/franco/Documments/pydocs/app/app1.py
/Users/franco/Documments/pydocs/modules/google/bigquery.py
/Users/franco/Documments/pydocs/modules/google/special/ultrasecret.py
/Users/franco/Documments/pydocs/main.py 
if you want to import a function from bigquery into app1.py this is the import in app1.py

# inside the module (or any python file we can use the special variable 
__name__
# to know (it's set at the beggining of the execution by python internals) which is the module (file) executing the beauthy of this
# is that if this module if executed directly 
python3 module.py 
# this variable is set as "__main__" this is useful for example to execute test directly in the file

import sys
def alwaysOne(a):
    a==1
    pass
if __name__ == "__main__":
    alwaysOne(1)==1 # redundant this function with any argument is defined to always return 1
    print "¡No hagas eso!" # even though we encourage the user to not run this file directly
    sys.exit()
    
# if its ran from a module (import from another file an acceses) __name__ is not "__main__"
whe way it should be imported is (after setting the path)
>> aoo1.py
import modules.bigquery 
or
from modules import bigquery # could we use as too
or 
from modules import bigquery.function # as it would work 
or
from modules import bigquery.special.function or import modules.bigquery.special.function # as recommended 
 
# Modules always should include a line to inform how should be run at the start of the file, for some systems this is useful (web page for instance)
#! /usr/bin/env python3 #! the sharp is because is a comment, and the ! is required, this is called shabang, sheband, hasbang, poundbangy hashplingd

# we encouraget that Modules incude a comment of what it does, purpose, etc

#### INIT #### __init__.py
# In order to import correcly (?) packages from folders those should be initialized with a __init__.py file helper
# empty if you don't know what to put inside, but it sould exists in every folder from where you want import modules

# python execution generate a file .pyc for internal python purposes ( is compiled or interpreted )
# this is machine code for python

##############
##### PIP ####

# It's recommended that PIP gets installed through the OS package manager
# PIP is an acronym ( Pip Installs Packages ) and is recursive like LINUX ( Linux Is Not UniX )
# Get pip version
> pip --version # if python2 is default
> pip3 --version # python3 command (new standard)
# dependencies hell is when your code has a lot of dependencies included and is hard to track them trough the code

pip help # shows a list of commands where pip can help you understand
pip help list # example of getting help with the list command of pip

pip list # shows the complete list of the packages installed until now

pip show name_of_the_package # a more detailed output of the name_of_the_package, notice location ( means that is installed ?)  

pip search anystring # anystring will be serached in all the packages ( in PyPI ) and in any summary string of the same packages, this is not case sensitive

pip install --user name_of_the_package # this will take note that you want to run this only for your user ( this is usefult when you have no admin permissions )

pip install -U name_of_the_package # this will update name_of_the_package to the last version, ( this command has --user implicit )

pip install name_of_the_package==package_version # this will install name_of_the_package with the specific package_version

pip uninstall name_of_the_package # this will uninstall name_of_the_package, and do whatever needs to do to clean that out

###################
####### OOP #######
__dict__                # variable that all objects have to know its properties and methods defined, this not includes class variables
        objOfCalss = classOne()
        print(objOfCalss.__dict__)

__name__                # this refers to the name of the class, objects do not have this, returns a string

__module__              # the name of the module(remeber files, namespaces, packages, etc) that contains the class

__bases__               # returns a tuple of clases (not names, clases per se), objects do not have this

type()          # shows what class was used to instance an object

self            # inside a class this has to be a parameter for every function (formaly methods) in the same class, varibales of the objects 
                # should be declared as self.var_name, inside the class is used to access the instance of the object and the variables of the class
                # self can be used to call another methods of the same class

## the OBJECT class is the parent of a class that has no inheritance




__ f.py
class oneClass:
        pass
        
        def modOne(self):
                pass
__

self.__name_ofVar               # this is how a encapsulation is done in python, the variable this way can only contain an aditional underscore _

__ f.py
class SuperClass:               ## This his how a class heritates properties, methods of another class
        pass
class NormalClass(SuperClass):
        pass
__

__ f.py
class oneClass(ZeroClass):               # in case that this class inheritates from another, the class should be passed as argument
        def __init__():         # this is how the constructor is created, this is the first thing executed one an object of the clases is intanciated, contructor cannot return a value              
                self.my_var="always first"
                ZeroClass.__init__(self)          # this is how the superclass constructor is initializated, ZeroClass it will be referenced as is futher to access their 
                s and properties
                
__
## Instance Variables ##
# a private varible could be accessed throug the reference of it object and its class, these could be verified with the __dict__ property of the instance object
obj1 = classUnknown()           # supose that onside that class the constructor has 1 private variable self.__varUnknown='Secret'
print (obj1._classUnknown____varUnknown)                # the value is accessed and printed

# if a variable is declared out of constructor, for instance after an object is intanciated the variable is accessed as a regular property, these could be verified with the __dict__ property of the instance object
obj1 = classUnknown()
obj1.__isprivate=2
print (obj1.__isprivate)

## class variables ##
does not require an object to exist, and its shared between all objects of the class
this variable always shows the same value for all instances
__ f.py
class ExampleClass:
        counter=0               # any instance of example class it will have the same value, if any method modifies the variable, all the intances can see that
        def __init__(self):
                pass
        def somFun(self):
                pass

obj1 = ExampleClass()
print (obj1.counter)
__

__ f.py         # default strings when trying to look objects without prints or get methods
class x:
        def __str__(self):              # is an object is instanciated alone of a clas
                print ("something")

y = x()
y               # this will print "something# by default
__


Access to a atribute of an object what doesn't exists will rise the AttibuteError

hasattr(class_or_object,"attribute")                 # this will check if an attribute exists in a class/object, the first argument is the class/object, the second is the attribute to check

getattr(obj,name)               # gets the value of an attribute
setattr(obj,name,value)                 # change the value of an attibute

#############################################
#### properties decorator setter getters ####
https://www.pythonmorsels.com/screencasts/properties/
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, location):
        self._location = location
        self.past_locations.append(location)

    trey = Person("Trey", "San Diego")
    trey.location
    >'San Diego'
    trey.location = "Portland"
    trey.location
    >'Portland'


########################
###### inheritance #####

issubclass(ClassOne, ClassTwo)          # returns true if a ClassOne is subclass of ClassTwo, every class is subclass of itself

isinstance(objectName, ClassName)               # returns True if objectName is instance of ClassName, remember when ClassName has been inherited from another the other it would be istance of the object too

is                     # This operator compares to objects ( memmory references actually ), for example list, strings wuold return true
object_one is object_two

super().__init__(optional_param)                # super is useful to access to the superclass without knowing its name, any resource, contructor, methods, properties

# Overrride
__ f.py
class SubClass(Left,Right):             # if there are multiple varaibles with the same name (because of inheritance), the name that remains is the one more "close" (immediate super class or the class itself if it has the variable) to the object instanciated, this applies equal to the methords
        pass                            # if there are multiple classes inheriting and those have methods and/or vars with the same name the priority if from left to right in the class cl4ssX(Left,Right,Right2,Right3):
        
__        

# Polymorphism                                  ## When a subclass can modify its superclass behaviour this is called polymorphism 
__ f.py
class One:
    def do_it(self):                            ## this method is changed by the one int class Two
        print("do_it de One")                   

    def doanything(self):                       ## This method is inheritated 
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it de Two")


one = One()
two = Two()

one.doanything()
two.doanything()

>> do_it de One
>> do_it de Two
__

MRO             # MRO means  Methods Resolution Object, and is in charge of checking correct multiple inheritance 


#########################################
###### Generadores / Iteradores #########

Un iterador debe proporcionar dos metedos __iter__() y __next__() esto es leido por los FOR y los IN para ir avanzando

_ f.py #Esto es un iterador de la serie de fibonacci
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10): # el for lee la clase directo es como haber implementado el iterador range
    print(i)
_

yield x         # it goes like the "return x" # This GENERATOR OBJECT (is not a function)
                # is used transform functions into generators and doesn't loose the state of the function
                # all the values get frozen until the next invocation

# list and generators in a list comprenhension

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]          # this creates a list
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))             # this creates a generator, is not the same as a list, e.g. a generator dows not have a len(generator_x) function, it would rise a TypeError exeption ( len doesn't support generators )

#################
#### LAMBDA #####

Anonimous functions, basic definitinon:

lambda parámetros entrada: expresión, regresa la evaluación

lambda x: 2 * x**2 - 4 * x + 2 

: SAME AS :

def poly(x):
    return 2 * x**2 - 4 * x + 2
    
PEP 8
def f():
        something # This is BETTER than
        
f = lamda x: something # the asignacion of f as the name of function, def is recommended by python guys, but still a recommendation
        

################# 
####### MAP #####

# This function will apply the "function" the elements of the second argument, it returns an iterable

map(function, list)             # It takes two arguments, a function and a list ( an iterable actually )
                                # the second argument could be any itarable, a tupple, a generator etc, and its a copy of the original object
                                # map could take more than two arguments

###################
####### Filter ####

filter(function_x, iterable_y)

# This function is similart to the map function, the difference is that this will wipeout all the calues that don't 
# meet the conditions of the first argument (function) over the second argument (an iterable), the second argument gets a copy of the original "iterable"

filter(lambda x: x > 0 and x % 2 == 0, data)            # the anonimous function "lambda" is the function to filter the iterable "data"

###############################
###### Cierre / Clousure ######

# It hast to be a function nested function and have to be returned to keep a frozen copy in memory of 
# the state of the function from where it was returned, even if the original context doesn't exists anymore
# A clousure has to be invoked as originally was

_ f.py
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)
# Multiplier of 5
times5 = make_multiplier_of(5)
# Output: 27
print(times3(9))
# Output: 15
print(times5(3))
# Output: 30
print(times5(times3(2)))
_


#######################
###### METHODS ########

# methods can be named starting with __methodname, a method like this is a hidden method ( partialy )
# a hidden method will not be available out of the class, the only exception is when you call it with the format obj._class__hidden_method()

######################
###### Streams ######

# There are two operations in streams
        - read 
        - write
# There are three basic modes to open a stream
        - read
        - write
        - update

# Clases, these three will be invoked by the open() function, to discard this object the function close() should be invoked
        - IOBase
                - RawIOBase
                - BufferedIOBase (* most used in this course)
                - TextIOBase (* most used in this course)
# Stream clasess are of two basic types
        - text ( structured in character or lines) 
        - binary ( structured in bytes or blocks(defined) )

# Program portability for text is automatilly handled by the stream clases, windows uses and end line las CR LF (\r\n) and Unix/Linux uses only LF (\n), this clases handle this to unify all as Unix

# Functions & Methods

        stream = open(file, mode = 'r', encoding = None)
        
                - FileNotFoundError is file is missing 
                - file is the name of the file to be used ( read/write ) (MANDATORY)
                - mode is r (rt), w (wt), ab (binary append) etc. (default r)
                - enconding, remember the ascii (default depends on the System configuration)

Modo    Modo      
texto   binario   Descripción
rt      rb        lectura       # file should exists or open() will rise an exception (Default)
wt      wb        escritura     # file will be created/replaced, open will rise an exception if permission are insufficent
at      ab        adjuntar      # file will be created if exists it will point at the end to append
r+t     r+b       lectura y actualización       # file should exists and allow write operations otherwise an exceptions will be rised
w+t     w+b       escritura y actualización     # if file doesn't exists it will be created, existing content will be intact if exists
x       xb        solo creacion # this will only create the file



        stream.close() # it closes the stream
                - Beware of the stream some times the physical object might be slow and when the close happens before the stream finished 
                  writing(/reding?) this might cause an exception
        
# Special pre open streams, there is no need to close 
        
        sys.stdin ( input stream, normally the keyboard)
        sys.stdout ( output stream, normally the screen)
        sys.stderr ( error stream, defaut the output on the screen but not all)

# Error exceptions 
from os import sterror
try:
    # Algunas operaciones con streams.
except IOError as exc:
    print(exc.errno)
errno.EACCES - Permission denied, this could happend when trying to write a read only stream
errno.EBADF - File number incorrect, this happens normally when a stream is trying to be used and is not instanciated
errno.ENOSPC - No space left in the device
......

# strerror( ERRORNUM ) This will return a string description of the error, ERRORNUM input is the error id, if the id error does not exists, ValueError would be rised
        strerror(exc.errno)

# read method will send the stream to the standard output
        stream.read()   # reads, remmember thinking about the memmory before reading a HUGE file, 
                        # it could lead to a memmory overflow
                        # This is an ITERABLE
        stream.read(1)  # reads the first character
        stream.read(1)  # if this if after another read(1) it will read the 2nd character and so on, 
                        # following the pointer concept on the stream
        stream.readline()       # It returns a complete text line, if there is no more an empty line will be returned
        stream.readline(1)      # Same as stream.read(1) the pointer to the last line read would work the same
                                # Its an iterable
        stream.readlines(20)    # When this is instanciated it tries to return a LIST (an iterable) of strings, an element of the list by each line in the file
                                # When all has been read and there is no more it will return an empty list (len(x)==0)
                                # the parameter set as input (20) is the number of bytes to be read, this might lead to a better performance than read each line or each character at the time

# Using open() as an iterable
# This might be useful for some cases, this function will return by default an iterable and the private method __next__ will return the next line, so it goes line by line
# and when its over it will close the stream automatically
_ f.py
for line in open('text.txt', 'rt'):
		line_counter += 1
		for char in line:
			print(char, end='')
			character_counter += 1
_

        stream.write("SomeString\n") # When trying to write a line break it has to be explicit sending \n

## bytearray
# another way to store data what is not text, we use bytearray streams (this is not binary yet)
        
        data = bytearray(10)    # This will create an object bytarray type of 10 bytes, array full of 0's
                                # every value in the array should be an integer in the range 0-255, otherwise ValueError will be rised

        binary_file = open('file.bin', 'wb')    # Writeable file in binary mode
        binary_file.write(data) # This will write the bytearray into a binary file
        binary_file.close()     # always close you files explicitly
        readinto(data)  # This will use the binary file (read previously with open) and don't create a new one, this is the way how a binary file is read
        binary_file.read() # this will read all the data from a binary file, take count the size of the file, you don't want to consume all the memory (hopefully)
                # Example
                binary_file = open('file.bin', 'rb')    # Readiing the binary file
                data = bytearray(binary_file.read(5))    # asigning a byte array to makeit iterable (?), 5 will limit the number of bytes to be read, to determine how many bytes 
                                                         # finally were read len(x) shold be used, remember that the pointer still is pointing to the last read byte and is waiting to continue reading
                binary_file.close()     # closing the original file

####################
######## OS ########

OS is a python module to interact with the operating system

os.uname()	# it returns an object whith the systemname, nodename, release, version and machine
os.name()	# returns the name of the operating system, LINUX(posix), WINDOWS (nt), java (Jython)
os.mkdir("my_dir")	# creates at the current directory (where the python program was launched) my_dir folder, if exists it will rise an FileExistsError, absolute directories are allowed too
os.makedirs("my_dir/my_inner_dir") # Same as mkdir but it will create multiple folders with one command, if the last folder exists exception will be rised
os.getcwd()	# returns the current working directory absolute rute
os.rmdir("my_first_directory")	# delete a directory, error if folder is not empty
os.removedirs("my_first_directory/my_second_directory")	# delete multiple directories, error if folder is not empty

## System ##
# system will interact with the current operating system, Unix will return the output result of the command meanwhile Windows will return the console result
os.system("mkdir my_dir") 	# it will launch the command in linux and returns a 0 because is the succes output of that
os.system("ls -la")	# It will list all the current files/directories in the directory, returns a 0 as a result of success

##########################
######## datetime ########
import datetime

datetime.date 	# objects in this class represent a date with year, month and day, this object is read only
datetime.date.today()	# has 3 attributes, year, month and day
	today = datetime.date.today()
		today.year
		today.month
		today.day
# to create a date object you need to instance an object of the class date and then pass the parameters year, month and day
from datetime import date
my_date = date(2019,11,4)
	# year must be between 1 and 9999
	# month between 1 and 12
	# day between 1 and the last day of month and year defined, think of leap years

## time ## In windows and Unix Leap seconds doesn't count
import time
time.time() # this will return the difference between 1970-01-01 00:00:00 and the current time in seconds
	# 1650139684.3529685 for example
from datetime import date
date.fromtimestam(time.time()) # this will return the current date
	# 2022-04-16 for example, note that this has no time
date.fromisoformat("2019-11-04") # ISO 8601 defines YYYY-MM-DD format, numbers below 10 should lpad with 0 at 2 characters, 
				 # this will take that date and transform it to a date object
new_date_ob = date_obj.replace(year=1992,month=1,day=1)	# remember that the date object is inmutable so it has to be asigned to another variable
							# the year, month and day are optional, if none is passed same date will be returned, from python 3.7
date_obj.weekday()	# this method it will return the number of day of the week, 0 Monday to 6 Sunday
date_obj.isoweekday()	# this method it will return the number of day of the week in ISO 85601 format, Monday 1 to 7 Sunday

## Time ##
from datetime import time

time(hour, minute, second, microsecond, tzinfo, fold) # this parameters are optional, remember that this is not a datetime object
	# hour 0-23
	# minute 0-59
	# second 0-59
	# microsecond 0-1000000
	# subclass object of tzinfo or None (default)
	# 0-1 default 0

## datetime ##
# In the module datetime is the class to combine date and time objects
datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold) # remember positional and defined arguments
	year 1-9999
	month 1-12
	day 1-last day of month/year (think of leap years)
	hour 0-23
	minute 0-59
	second 0-59
	microsecond 0-1000000
	tzinfo # should be subclass of tzinfo or None
	fold 0-1, default 0
	
from datetime import datetime
dt = datetime(2019, 11, 4, 14, 53)
	# 2019-11-04 14:53:00 returns

# datetime module has multiple useful methods 
from datetime import datetime
datetime.today()	# Current date with time and microseconds, with tzinfo set to None
	# 2022-04-16 17:46:31.671519
datetime.now()		# Current date with time and microseconds, this acepts a tzinfo parameter
	# 2022-04-16 17:46:31.672871
datetime.utcnow()	# UTC date and time with microseconds, tzinfo set to None
	# 2022-04-16 22:46:31.673748
datetime_obj.timestamp() # returns the timestamp of the datetime object
	# dt = datetime(2020, 10, 4, 14, 55)
	# dt.timestamp()
	# 1601823300.0

## strftime ##
# all the datetime clases have a strftime function to return a date into a desired format 
datetime_obj.strftime("format_string") # format https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
from datetime import datetime
from datetime import time
	#d=date(2929,01,01)
	#d.strftime("%Y/%m/%d")
	#2929/01/01
	#t=time(14,53)
	#t.strftime("%Y:%H:%M:%S")
	#1900:14:53:00

## strptime ##
# this method will transform a string into a datetime object
from datetime import datetime
datetime.strptime("stringToTransform","FormatToInterpretTheString")
	x = datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S") # x will be a datetime.datetime class object
	
## Operations with date and times 
operations with dates or times will create a timedelta object
date - date2 -> timedeltaobject

## TimeDelta ##
from datetime import timedelta
delta = timedelta(weeks=2, days=2, hours=3) # numbers could be >0, float, or negative, internally timedelta objects only store days, seconds and microseconds
					    # intervals always will always be shown as complete days, hours minutes etc (this is independently of how is stored)
	# posible optional arguments are:
	# days
	# seconds
	# microseconds
	# miliseconds
	# minutes
	# hours
	# weeks

delta_obj * int -> int (times) delta_obj
date_obj + timedelta_obj -> date
datetime_obj + timedelta_obj -> datetime



	
######################
######## TIME ########

# Time as a module exists too, includes some useful functions too
import time
time.sleep(x)	# where X is an int or float, it will hold the execution of the program x seconds and then continue the execution
time.ctime(unixtimestamp)	# this will take a unix timestamp and convert it to a date (not iso format), default is now (like datetime.time.time() )
	# Sat Apr 16 20:54:37 2022, for example

time.time() # current unixtimestamp
time.struct_time: ## definition of the class struct_time, contructor
    tm_year   # Especifica el año.
    tm_mon    # Especifica el mes (valor de 1 a 12)
    tm_mday   # Especifica el día del mes (valor de 1 a 31)
    tm_hour   # Especifica la hora (valor de 0 a 23)
    tm_min    # Especifica el minuto (valor de 0 a 59)
    tm_sec    # Especifica el segundo (valor de 0 a 61)
    tm_wday   # Especifica el día de la semana (valor de 0 a 6)
    tm_yday   # Especifica el día del año (valor de 1 a 366)
    tm_isdst  # Especifica si se aplica el horario de verano (1: sí, 0: no, -1: no se sabe)
    tm_zone   # Especifica el nombre de la zona horaria (valor en forma abreviada)
    tm_gmtoff # Especifica el desplazamiento al este del UTC (valor en segundos)
    
time.gmtime(unixtimestamp)	# This will return an struct_time UTC object, tm_isdst=0 always for GMT, and this could be accessed by index
time.localtime(unixtimestamp)	# This will return an struct_time local time object, and this could be accessed by index
	# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0) Example of the object content
time.gmtime(unixtimestamp)	# converts a unixtimestamp or a tupple into a string
time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)) # it converts an struct_time objecto or a tuple witch express local time into a number of seconds unixtimestamp (sinnce 19700101)
	2019 => tm_year
	11 => tm_mon
	4 => tm_mday
	14 => tm_hour
	53 => tm_min
	0 => tm_sec
	0 => tm_wday
	308 => tm_yday
	0 => tm_isdst

### strftime ###
# time_class.strftime FUNCTION
# ths function will transform a time object to a desired format, https://docs.python.org/3/library/time.html#time.strftime
import time
timestamp = 1572879180
st = time.gmtime(timestamp)
print(time.strftime("%Y/%m/%d %H:%M:%S", st))	# here the second argument if the struct_time to be formated
	# 2019/11/04 14:53:00 this is printed
print(time.strftime("%Y/%m/%d %H:%M:%S"))	# if none struct_time is passed then the current_time is formated
	# 2022/04/16 23:06:54 this is printed

### strptime ###
# time_class.strptime FUNCTION
time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")
	# this will return time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)


##########################
######## Calendar ########
# this is another moduloe
import calendar

# it has this contants corresponding an integer value
Day		Value	Constant
Monday		0	calendar.MONDAY
Tuesday		1	calendar.TUESDAY
Wednesday	2	calendar.WEDNESDAY
Thursday	3	calendar.THURSDAY
Friday		4	calendar.FRIDAY
Saturday	5	calendar.SATURDAY
Sunday		6	calendar.SUNDAY

# Months have integer values from 1-12 (January-December)

# calendar function
import calendar
print(calendar.calendar(2022))	# This will print a complete calendar of a year, graphically
	# calendar has this parameters
	w column width,separating days, (graphically), default 2
	l number of lines separating weeks (graphically), default 1
	c number of spaces beteen months (graphically), default 6
	m number of columns (graphically), defaylt 3
calendar.prcal(2022)	# same as past is not necesary to print explicitly

print(calendar.month(2022,11))	# this will print only a month
calendar.prmonth(2022,11)

calendar.setfirstweekday(calendar.SUNDAY) 	# change the initial day of the week, using the constant, 6 could be sent too
calendar.prmonth(2020, 12) # prints a full month starting with sunday

import calendar
print(calendar.weekday(2020, 12, 24))
	# it returns a 3, that a thursday

import calendar
print(calendar.weekheader(2)) # this will print the new week header (default 3) now with the characeter length, 
			      # this is affected if setfirstweekday is set
			      # only shows week headers, nothing else

calendar.isleap(2020)	# this will print True or false if the parameter is a leap year

calendar.leapdays(2010, 2020)	# quantity of leap years year, not including the upper limit
	# Between 2010 and 2020 there are 3(2012,2016,2020) leap years but as the upper limit is not included this will print 2

# extra calendar clases
calendar.Calendar	# gives methods to prepare calendar data and give format
calendar.TextCalendar	# regular text calendars
calendar.HTMLCalendar	# HTML calendars
calendar.LocalTextCalendar	# subclass of TextCalendar but it has a variable with the locale, to transform month names and day names

calendar.Calendar(calendar.SUNDAY) 	# This will create a calendar with the first day of the week set to Sunday
for weekday in c.iterweekdays():	# iterweekdays is an iterator of calendar with the days of the week 
	print(weekday,end=' ') 	# here the numbers will be printed as 6 0 1 2 3 4 5

c.itermonthdates(2019, 11) 	# Is another iterator returns dates of a month ant if the start and end of the month
				# does not includes a full week, aditional dates will be returned to recive complete weeks

c.itermonthdays(2019, 11)	# this returns the days of the week, same behaviour as itermonthdates but the days that are not in the desired month will be 0
c.itermonthdates2(2019, 11)	# it will return tuples with the day of week and day of month
c.itermonthdates3(2019, 11)	# Python 3.7 returns a tuple with year, month, day
c.itermonthdates4(2019, 11)	# Python 3.7 returns a tuple with year, month, day, day of week

https://docs.python.org/3/library/calendar.html

calendar.monthdays2calendar(2022,4)	# this will return by week a list of tuples with the day of the month and the daynumber, remember the 0 in the daynumber 
					# is for days not included in the month the "relleno" ones





##########################
######## SNIPPETS ########
##########################

###############
# copy a file into another #

in_file = open(from_file)
indata = in_file.read()
out_file = open(to_file,'w')
out_file.write(infile)
in_file.close()
out_file.close()

###############
# copy in one line, auto close #
open( to_file , 'w' ).write( open( from_file ,'r' ).read() )

###############
# write strings to a file
f = open("live_reports_imports.txt", "a")
f.write(query)
f.close()

#############################################
# copy two files, user input
_ f.py
from os import strerror

source_file_name = input("Ingresa el nombre del archivo fuente: ")
try:
    source_file = open(source_file_name, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

destination_file_name = input("Ingresa el nombre del archivo destino: ")
try:
    destination_file = open(destination_file_name, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino:", strerror(e.errno))
    source_file.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = source_file.readinto(buffer)
    while readin > 0:
        written = destination_file.write(buffer[:readin])
        total += written
        readin = source_file.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
source_file.close()
destination_file.close()
_


###################
###### PANDAS #####
###################

## Find and fill [ IN ( LIKE OR LIKE ) ]
#is_contact is the field to be filled with '1' depending on a 
#set of regular expressions declared to search in cat column in x DataFrame
oro_tks.loc[ oro_tks.DSC_Second_Subcategory_CS.fillna('0').str.contains('^1.6.19*|^1.6.18*|^2.6.3*',regex = True).fillna(True) ,'Is_Contact'] = 1

## Pivot Table
## ['label','monthnum_finance','prefix'] -> Dimensions
## ['NMV','skus_sold','fk_seller'] -> Metrics
## 'NMV':['sum','mean',q1,q2,q3] -> functions applied to metrics, q1 represents a funtion outside:
''' 
    def q1(x):
    return x.quantile(0.25)
'''
df.groupby(['label','monthnum_finance','prefix'])['NMV','skus_sold','fk_seller'].agg({
                                                                                             'NMV':['sum','mean',q1,q2,q3],
                                                                                             'skus_sold':['sum','mean',q1,q2,q3],
                                                                                             'fk_seller':'nunique'
                                                                                            })
                                                                                            
## Simple Filter
## debit column grater than 0
## Just Returning debit column

data[data.debit<0]['debit']
                        

##### Number format all dataframes
##### Configure to display numbers with a 2 deciaml format instead of scientific notation

pd.options.display.float_format = '{:.2f}'.format

##### Unique Values of a dataframe columns
df.column.unique()

#### Values of a colun to list
df.column.tolist()
## Unique
df.column.unique().tolist()

#### Values of a dataframe column into a string separated with , (or other character)
",".join( "" + str( i ) + ""  for i in  df.column.unique().tolist() )

## flat groupped column names
complete.columns = ['_'.join(col) if type(col)==tuple else col for col in complete.columns.values ]


Useful resources:
https://www.pythonmorsels.com/articles/
